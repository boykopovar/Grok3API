from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, FrozenSet, List, Optional, Set, Tuple



FieldDef = Tuple[int, str, str, bool]
EnumDef = List[Tuple[str, int]]
GlobalEnums = Dict[str, EnumDef]
GlobalMsgs = Dict[str, List[FieldDef]]
PerFile = Dict[str, Tuple[GlobalEnums, GlobalMsgs]]

_PROTO_DIR_DEFAULT = Path("docs/proto")
_OUT_PKG_DEFAULT = "grok3api/types/proto"

_W_STRING = "WireType.STRING"
_W_BOOL = "WireType.BOOL"
_W_INT32 = "WireType.INT32"
_W_INT64 = "WireType.INT64"
_W_FLOAT = "WireType.FLOAT"
_W_DOUBLE = "WireType.DOUBLE"
_W_BYTES = "WireType.BYTES_FIELD"
_W_TS = "WireType.TIMESTAMP"
_W_EMPTY = "WireType.EMPTY_MESSAGE"
_W_JSTRUCT = "WireType.JSON_STRUCT"
_W_JVALUE = "WireType.JSON_VALUE"
_W_FMASK = "WireType.FIELD_MASK"
_W_MAP = "WireType.MAP_FIELD"
_W_REP_STR = "WireType.REPEATED_STRING"
_W_REP_MSG = "WireType.REPEATED_MESSAGE"
_W_MESSAGE = "WireType.MESSAGE"

_PY_STR = "str"
_PY_BOOL = "bool"
_PY_INT = "int"
_PY_FLOAT = "float"
_PY_BYTES = "bytes"
_PY_DICT = "dict"
_PY_OBJ = "object"

_PROTO_STRUCT = "google.protobuf.Struct"
_PROTO_VALUE = "google.protobuf.Value"
_PROTO_EMPTY = "google.protobuf.Empty"
_PROTO_FMASK = "FieldMask"

_DEF_FACTORY_LIST = "Field(default_factory=list)"
_DEF_FACTORY_DICT = "Field(default_factory=dict)"

_IMPORT_PB_META = "grok3api.types.pb_meta"
_IMPORT_PROTO_PKG = "grok3api.types.proto"

_SHARED_MODULE = "shared"
_ENCODING = "utf-8"
_INIT_FILE = "__init__.py"

_PFX_LIST = "List["
_PFX_OPT = "Optional["

_SCALAR_WIRE: Dict[str, str] = {
    "string": _W_STRING,
    "bool": _W_BOOL,
    "int32": _W_INT32,
    "uint32": _W_INT32,
    "sint32": _W_INT32,
    "fixed32": _W_INT32,
    "sfixed32": _W_INT32,
    "int64": _W_INT64,
    "uint64": _W_INT64,
    "sint64": _W_INT64,
    "fixed64": _W_INT64,
    "sfixed64": _W_INT64,
    "float": _W_FLOAT,
    "double": _W_DOUBLE,
    "bytes": _W_BYTES,
}

_SCALAR_PY: Dict[str, str] = {
    "string": _PY_STR,
    "bool": _PY_BOOL,
    "int32": _PY_INT,
    "uint32": _PY_INT,
    "sint32": _PY_INT,
    "fixed32": _PY_INT,
    "sfixed32": _PY_INT,
    "int64": _PY_INT,
    "uint64": _PY_INT,
    "sint64": _PY_INT,
    "fixed64": _PY_INT,
    "sfixed64": _PY_INT,
    "float": _PY_FLOAT,
    "double": _PY_FLOAT,
    "bytes": _PY_BYTES,
}

_WELL_KNOWN_WIRE: Dict[str, str] = {
    _PROTO_STRUCT: _W_JSTRUCT,
    _PROTO_VALUE: _W_JVALUE,
    _PROTO_EMPTY: _W_EMPTY,
    _PROTO_FMASK: _W_FMASK,
}

_WELL_KNOWN_PY: Dict[str, str] = {
    _PROTO_STRUCT: _PY_DICT,
    _PROTO_VALUE: _PY_OBJ,
    _PROTO_EMPTY: _PY_BOOL,
    _PROTO_FMASK: f"{_PFX_LIST}{_PY_STR}]",
}

_TIMESTAMP_SUFFIXES: Tuple[str, ...] = (
    "_time",
    "_at",
    "_after",
    "_before",
    "expires_at",
    "created_at",
    "updated_at",
    "deleted_at",
    "heartbeat_time",
)

_RESERVED_PY: FrozenSet[str] = frozenset({
    "from", "import", "class", "def", "return", "if", "else", "elif",
    "for", "while", "in", "is", "not", "and", "or", "True", "False", "None",
    "lambda", "with", "as", "try", "except", "finally", "raise", "pass",
    "break", "continue", "global", "nonlocal", "del", "yield", "assert",
    "type", "list", "dict", "set", "tuple", "str", "int", "float", "bool",
    "bytes", "object", "super", "self", "cls",
    "id", "input", "print", "len", "range", "open", "format",
})

_WIRE_DEFAULTS: Dict[str, str] = {
    _W_BOOL: "False",
    "WireType.OPT_BOOL": "False",
    _W_INT32: "0",
    _W_INT64: "0",
    _W_FLOAT: "0.0",
    _W_DOUBLE: "0.0",
    _W_STRING: '""',
    _W_BYTES: 'b""',
    _W_TS: '""',
    _W_EMPTY: "False",
    _W_JSTRUCT: _DEF_FACTORY_DICT,
    _W_JVALUE: "None",
    _W_FMASK: _DEF_FACTORY_LIST,
    _W_MAP: _DEF_FACTORY_DICT,
}

_RE_ENUM_BLOCK = re.compile(r"\benum\s+\w+\s*\{")
_RE_MSG_BLOCK = re.compile(r"\bmessage\s+\w+\s*\{")
_RE_FIELD = re.compile(r"\b(repeated\s+)?([\w.]+)\s+(\w+)\s*=\s*(\d+)\s*;")
_RE_ENUM_VAL = re.compile(r"(\w+)\s*=\s*(\d+)\s*;")


def _safe_name(name: str) -> str:
    return name + "_f" if name in _RESERVED_PY or name.endswith("_") else name


def _strip_comments(text: str) -> str:
    text = re.sub(r"//[^\n]*", "", text)
    return re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)


def _extract_block(text: str, start: int) -> str:
    depth = 1
    i = start
    while i < len(text) and depth:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    return text[start: i - 1]


def _strip_nested(body: str, pattern: re.Pattern) -> str:  # type: ignore[type-arg]
    flat = body
    while True:
        m = pattern.search(flat)
        if not m:
            break
        inner = _extract_block(flat, m.end())
        flat = flat[: m.start()] + flat[m.start() + len(m.group()) + len(inner) + 1:]
    return flat


def _parse_direct_fields(body: str) -> List[FieldDef]:
    flat = _strip_nested(_strip_nested(body, _RE_ENUM_BLOCK), _RE_MSG_BLOCK)
    return [(int(m.group(4)), m.group(2), m.group(3), bool(m.group(1))) for m in _RE_FIELD.finditer(flat)]


def _parse_proto(text: str) -> Tuple[GlobalEnums, GlobalMsgs]:
    enums: GlobalEnums = {}
    msgs: GlobalMsgs = {}

    def collect_enums(body: str, prefix: str) -> None:
        for m in _RE_ENUM_BLOCK.finditer(body):
            name = prefix + m.group(0).split()[1]
            eb = _extract_block(body, m.end())
            enums[name] = [(vm.group(1), int(vm.group(2))) for vm in _RE_ENUM_VAL.finditer(eb)]

    def collect_msgs(body: str, prefix: str) -> None:
        for m in _RE_MSG_BLOCK.finditer(body):
            flat_name = prefix + m.group(0).split()[1]
            inner = _extract_block(body, m.end())
            collect_enums(inner, flat_name)
            collect_msgs(inner, flat_name)
            msgs[flat_name] = _parse_direct_fields(inner)

    collect_enums(text, "")
    collect_msgs(text, "")
    return enums, msgs


def _is_timestamp(field_name: str, py_type: str) -> bool:
    if py_type != _PY_BYTES:
        return False
    low = field_name.lower()
    return any(low.endswith(s) for s in _TIMESTAMP_SUFFIXES)


def _flatten_candidates(proto_type: str, owner_prefix: str) -> List[str]:
    if "." not in proto_type:
        return [owner_prefix + proto_type, proto_type]
    parts = proto_type.split(".")
    return [proto_type.replace(".", ""), parts[-1], owner_prefix + parts[-1]]


def _resolve_type(
    proto_type: str,
    field_name: str,
    is_rep: bool,
    owner_prefix: str,
    known_enums: Set[str],
    known_msgs: Set[str],
) -> Tuple[str, str, Optional[str]]:
    if proto_type in _WELL_KNOWN_WIRE:
        wire = _WELL_KNOWN_WIRE[proto_type]
        py = _WELL_KNOWN_PY[proto_type]
        return (_W_REP_STR, f"{_PFX_LIST}{py}]", None) if is_rep else (wire, py, None)

    if proto_type in _SCALAR_WIRE:
        wire = _SCALAR_WIRE[proto_type]
        py = _SCALAR_PY[proto_type]
        if _is_timestamp(field_name, py):
            return (_W_REP_STR, f"{_PFX_LIST}{_PY_STR}]", None) if is_rep else (_W_TS, _PY_STR, None)
        return (_W_REP_STR, f"{_PFX_LIST}{py}]", None) if is_rep else (wire, py, None)

    for candidate in _flatten_candidates(proto_type, owner_prefix):
        if candidate in known_enums:
            return (_W_REP_STR, f"{_PFX_LIST}{candidate}]", None) if is_rep \
                else (_W_INT32, candidate, None)
        if candidate in known_msgs:
            return (_W_REP_MSG, f"{_PFX_LIST}{candidate}]", candidate) if is_rep \
                else (_W_MESSAGE, f"{_PFX_OPT}{candidate}]", candidate)

    return (_W_REP_STR, f"{_PFX_LIST}{_PY_STR}]", None) if is_rep else (_W_STRING, _PY_STR, None)


def _default_value(py_type: str, wire: str, enum_vals: Optional[EnumDef]) -> str:
    if py_type.startswith(_PFX_LIST):
        return _DEF_FACTORY_LIST
    if py_type.startswith(_PFX_OPT):
        return "None"
    if enum_vals is not None:
        for vname, vval in enum_vals:
            if vval == 0:
                return f"{py_type}.{vname}"
        return f"{py_type}(0)"
    return _WIRE_DEFAULTS.get(wire, "None")


def _topo_sort(msgs: GlobalMsgs, all_msgs: GlobalMsgs) -> List[str]:
    order: List[str] = []
    visited: Set[str] = set()

    def visit(name: str) -> None:
        if name in visited:
            return
        visited.add(name)
        for _, ftype, _, _ in msgs.get(name, []):
            for candidate in [ftype.replace(".", ""), ftype.split(".")[-1]]:
                if candidate in msgs and candidate not in visited:
                    visit(candidate)
        order.append(name)

    for name in msgs:
        visit(name)
    return order


def _build_symbol_index(per_file: PerFile) -> Dict[str, str]:
    index: Dict[str, str] = {}
    for stem, (fe, fm) in per_file.items():
        for name in fe:
            index[name] = stem
        for name in fm:
            index[name] = stem
    return index


def _referenced_class_symbols(
    msgs: GlobalMsgs,
    all_enums: GlobalEnums,
    all_msgs: GlobalMsgs,
) -> Set[str]:
    known_enums: Set[str] = set(all_enums)
    known_msgs: Set[str] = set(all_msgs)
    result: Set[str] = set()
    for msg_name, fields in msgs.items():
        for _, proto_type, field_name, is_rep in fields:
            _, py_type, cls_ref = _resolve_type(proto_type, field_name, is_rep, msg_name, known_enums, known_msgs)
            if cls_ref:
                result.add(cls_ref)
            inner = py_type
            for pfx in (_PFX_LIST, _PFX_OPT):
                if inner.startswith(pfx):
                    inner = inner[len(pfx):]
            inner = inner.rstrip("]")
            if inner in known_enums or inner in known_msgs:
                result.add(inner)
    return result


def _collect_external_deps(
    enums: GlobalEnums,
    msgs: GlobalMsgs,
    all_enums: GlobalEnums,
    all_msgs: GlobalMsgs,
    symbol_index: Dict[str, str],
    own_stem: str,
    own_symbols: Optional[Set[str]] = None,
) -> Dict[str, Set[str]]:
    known_enums: Set[str] = set(all_enums)
    known_msgs: Set[str] = set(all_msgs)
    if own_symbols is None:
        own_symbols = set(enums) | set(msgs)
    deps: Dict[str, Set[str]] = {}

    def record(candidate: str) -> None:
        if candidate in own_symbols:
            return
        src = symbol_index.get(candidate)
        if src and src != own_stem:
            deps.setdefault(src, set()).add(candidate)

    for fields in msgs.values():
        for _, proto_type, field_name, is_rep in fields:
            _, py_type, cls_ref = _resolve_type(proto_type, field_name, is_rep, "", known_enums, known_msgs)
            if cls_ref:
                record(cls_ref)
            inner = py_type
            for pfx in (_PFX_LIST, _PFX_OPT):
                if inner.startswith(pfx):
                    inner = inner[len(pfx):]
            inner = inner.rstrip("]")
            if inner in known_enums or inner in known_msgs:
                record(inner)

    return deps


def _has_internal_forward_refs(msgs: GlobalMsgs, all_enums: GlobalEnums, all_msgs: GlobalMsgs) -> bool:
    known_enums: Set[str] = set(all_enums)
    known_msgs: Set[str] = set(all_msgs)
    local_msgs: Set[str] = set(msgs)
    order = _topo_sort(msgs, all_msgs)
    position = {name: i for i, name in enumerate(order)}

    for msg_name, fields in msgs.items():
        for _, proto_type, field_name, is_rep in fields:
            _, _, cls_ref = _resolve_type(proto_type, field_name, is_rep, msg_name, known_enums, known_msgs)
            if cls_ref and cls_ref in local_msgs:
                if cls_ref == msg_name or position.get(cls_ref, -1) > position.get(msg_name, -1):
                    return True
    return False


def _detect_cycles(per_file: PerFile, all_enums: GlobalEnums, all_msgs: GlobalMsgs) -> Set[FrozenSet[str]]:
    symbol_index = _build_symbol_index(per_file)
    file_deps: Dict[str, Set[str]] = {
        stem: set(_collect_external_deps(fe, fm, all_enums, all_msgs, symbol_index, stem).keys())
        for stem, (fe, fm) in per_file.items()
    }
    cycles: Set[FrozenSet[str]] = set()

    def dfs(node: str, path: List[str], on_path: Set[str]) -> None:
        on_path.add(node)
        path.append(node)
        for neighbour in file_deps.get(node, set()):
            if neighbour in on_path:
                cycles.add(frozenset(path[path.index(neighbour):]))
            elif neighbour not in {n for c in cycles for n in c}:
                dfs(neighbour, path, on_path)
        path.pop()
        on_path.remove(node)

    for stem in per_file:
        dfs(stem, [], set())
    return cycles


def _fmt_field_line(safe: str, py_type: str, meta: str, dval: str) -> str:
    return f"    {safe}: Annotated[{py_type}, {meta}] = {dval}"


def _fmt_meta(tag: int, wire: str, cls_ref: Optional[str]) -> str:
    if cls_ref:
        return f"ProtoField(tag={tag}, wire={wire}, cls={cls_ref})"
    return f"ProtoField(tag={tag}, wire={wire})"


def _render_enum(enum_name: str, values: EnumDef) -> List[str]:
    lines: List[str] = [f"class {enum_name}(IntEnum):"]
    if not values:
        lines.append("    pass")
    else:
        for vname, vval in values:
            lines.append(f"    {vname} = {vval}")
    return lines + ["", ""]


def _render_msg(
    msg_name: str,
    fields: List[FieldDef],
    all_enums: GlobalEnums,
    all_msgs: GlobalMsgs,
) -> List[str]:
    known_enums: Set[str] = set(all_enums)
    known_msgs: Set[str] = set(all_msgs)
    lines: List[str] = [f"class {msg_name}(BaseModel):"]
    if not fields:
        lines.append("    pass")
    else:
        for tag, proto_type, field_name, is_rep in sorted(fields, key=lambda x: x[0]):
            wire, py_type, cls_ref = _resolve_type(
                proto_type, field_name, is_rep, msg_name, known_enums, known_msgs,
            )
            safe = _safe_name(field_name)
            enum_vals = all_enums.get(py_type) if py_type in known_enums else None
            dval = _default_value(py_type, wire, enum_vals)
            lines.append(_fmt_field_line(safe, py_type, _fmt_meta(tag, wire, cls_ref), dval))
    return lines + ["", ""]


def _header_imports(use_annotations: bool, extra: List[str]) -> List[str]:
    lines: List[str] = []
    if use_annotations:
        lines += ["from __future__ import annotations", ""]
    lines += [
        "from typing import Annotated, List, Optional",
        "",
        "from enum import IntEnum",
        "from pydantic import BaseModel, Field",
        "",
        f"from {_IMPORT_PB_META} import ProtoField, WireType",
    ]
    lines += extra
    lines += ["", ""]
    return lines


def _generate_shared_module(
    shared_symbols: Set[str],
    all_enums: GlobalEnums,
    all_msgs: GlobalMsgs,
    symbol_index: Dict[str, str],
) -> str:
    enums = {k: v for k, v in all_enums.items() if k in shared_symbols}
    msgs = {k: v for k, v in all_msgs.items() if k in shared_symbols}

    ext_deps = _collect_external_deps(
        enums,
        msgs,
        all_enums,
        all_msgs,
        symbol_index,
        _SHARED_MODULE,
        own_symbols=shared_symbols,
    )

    extra_imports: List[str] = []
    for dep_stem, symbols in sorted(ext_deps.items()):
        extra_imports.append(
            f"from {_IMPORT_PROTO_PKG}.{dep_stem} import {', '.join(sorted(symbols))}"
        )

    use_annotations = _has_internal_forward_refs(msgs, all_enums, all_msgs) or bool(ext_deps)

    lines = _header_imports(use_annotations, extra_imports)
    for enum_name, values in enums.items():
        lines += _render_enum(enum_name, values)
    for msg_name in _topo_sort(msgs, all_msgs):
        lines += _render_msg(msg_name, msgs[msg_name], all_enums, all_msgs)
    return "\n".join(lines)


def _generate_module(
    stem: str,
    enums: GlobalEnums,
    msgs: GlobalMsgs,
    all_enums: GlobalEnums,
    all_msgs: GlobalMsgs,
    symbol_index: Dict[str, str],
    shared_module: Optional[str],
    shared_symbols: Set[str],
    use_annotations: bool,
) -> str:
    ext_deps = _collect_external_deps(enums, msgs, all_enums, all_msgs, symbol_index, stem)

    extra_imports: List[str] = []
    if shared_module:
        extra_imports.append(f"from {_IMPORT_PROTO_PKG}.{shared_module} import *")
    for dep_stem, symbols in sorted(ext_deps.items()):
        non_shared = symbols - shared_symbols
        if non_shared:
            extra_imports.append(
                f"from {_IMPORT_PROTO_PKG}.{dep_stem} import {', '.join(sorted(non_shared))}"
            )

    lines = _header_imports(use_annotations, extra_imports)

    for enum_name, values in enums.items():
        if enum_name not in shared_symbols:
            lines += _render_enum(enum_name, values)

    filtered_msgs = {k: v for k, v in msgs.items() if k not in shared_symbols}
    for msg_name in _topo_sort(filtered_msgs, all_msgs):
        lines += _render_msg(msg_name, filtered_msgs[msg_name], all_enums, all_msgs)

    return "\n".join(lines)


def _write(path: Path, content: str) -> None:
    path.write_text(content, encoding=_ENCODING)
    print(f"written: {path}")


def run(proto_dir: Path, out_dir: Path) -> None:
    proto_files = sorted(proto_dir.glob("*.proto"))
    if not proto_files:
        print(f"no .proto files in {proto_dir}")
        sys.exit(1)

    all_enums: GlobalEnums = {}
    all_msgs: GlobalMsgs = {}
    per_file: PerFile = {}

    for path in proto_files:
        text = _strip_comments(path.read_text(encoding=_ENCODING))
        fe, fm = _parse_proto(text)
        per_file[path.stem] = (fe, fm)
        all_enums.update(fe)
        all_msgs.update(fm)

    symbol_index = _build_symbol_index(per_file)
    cycles = _detect_cycles(per_file, all_enums, all_msgs)

    shared_symbols: Set[str] = set()
    shared_module: Optional[str] = None

    if cycles:
        shared_module = _SHARED_MODULE
        for stem in {s for cycle in cycles for s in cycle}:
            fe, fm = per_file[stem]
            shared_symbols.update(fe)
            shared_symbols.update(fm)

    out_dir.mkdir(parents=True, exist_ok=True)
    module_names: List[str] = []

    if shared_module:
        _write(
            out_dir / f"{shared_module}.py",
            _generate_shared_module(shared_symbols, all_enums, all_msgs, symbol_index),
        )
        module_names.append(shared_module)

    for path in proto_files:
        stem = path.stem
        fe, fm = per_file[stem]
        all_own = set(fe) | set(fm)
        if all_own and all_own <= shared_symbols:
            continue

        cyclic_file_dep = any(
            dep_stem in {s for cycle in cycles for s in cycle}
            for dep_stem in _collect_external_deps(fe, fm, all_enums, all_msgs, symbol_index, stem)
        )
        filtered_msgs = {k: v for k, v in fm.items() if k not in shared_symbols}
        use_annotations = cyclic_file_dep or _has_internal_forward_refs(filtered_msgs, all_enums, all_msgs)

        content = _generate_module(
            stem, fe, fm, all_enums, all_msgs,
            symbol_index, shared_module, shared_symbols, use_annotations,
        )
        _write(out_dir / f"{stem}.py", content)
        module_names.append(stem)

    _write(
        out_dir / _INIT_FILE,
        "\n".join(f"from {_IMPORT_PROTO_PKG}.{m} import *" for m in module_names) + "\n",
    )
    print(f"done: {len(module_names)} file(s)")


def main() -> None:
    proto_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else _PROTO_DIR_DEFAULT
    raw_out = sys.argv[2] if len(sys.argv) > 2 else _OUT_PKG_DEFAULT
    out_dir = Path(*raw_out.split(".")) if ("." in raw_out and "/" not in raw_out) else Path(raw_out)
    run(proto_dir, out_dir)


if __name__ == "__main__":
    main()
