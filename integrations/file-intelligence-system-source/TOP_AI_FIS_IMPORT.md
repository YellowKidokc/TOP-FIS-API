# Legacy FIS Import

Source:

```text
D:\GitHub\file-intelligence-system
```

Imported because MCP memory identified this as a prior File Intelligence System
with a validated deterministic semantic addressing layer.

## Preserved Files

```text
fis\nlp\semantic_scorer.py
fis\nlp\hash_codec.py
fis\nlp\meta_mapper.py
fis\nlp\path_heuristics.py
fis\nlp\context_classifier.py
```

## Promotion Decision

Promoted active, dependency-light files to:

```text
D:\GitHub\TOP AI FIS\agents\labelers\semantic_addressing
```

Not promoted yet:

```text
old watcher
old popup UI
old Postgres pipeline
dashboard_semantic.py
```

Reason: the useful part is the deterministic 10D scorer/hash/meta layer. The old
watcher previously ran too broadly, and the new hub should own scope, queue,
review gates, and execution.

