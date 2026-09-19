from pathlib import Path
import json

plugin_base = Path("plugins/hc-reasoning/skills/hc-reasoning")
mirrors = [["SKILL.md","SKILL.md"],["references/decision-review.md","references/decision-review.md"],["references/evidence-check.md","references/evidence-check.md"],["references/hc-index.md","references/hc-index.md"],["references/problem-framing.md","references/problem-framing.md"],["sources/provenance.md","sources/provenance.md"]]

errors = []
for root_rel, plugin_rel in mirrors:
    root_path = Path(root_rel)
    plugin_path = plugin_base / plugin_rel
    if not root_path.exists():
        errors.append(f"Missing root mirror: {root_path}")
        continue
    if not plugin_path.exists():
        errors.append(f"Missing packaged mirror: {plugin_path}")
        continue
    if root_path.read_bytes() != plugin_path.read_bytes():
        errors.append(f"Mirror drift: {root_path} != {plugin_path}")

for metadata in [
    Path(".agents/plugins/marketplace.json"),
    plugin_base.parent.parent / ".codex-plugin" / "plugin.json",
]:
    if not metadata.exists():
        errors.append(f"Missing plugin metadata: {metadata}")
        continue
    try:
        json.loads(metadata.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid JSON {metadata}: {exc}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(mirrors)} mirrored files and plugin metadata.")
