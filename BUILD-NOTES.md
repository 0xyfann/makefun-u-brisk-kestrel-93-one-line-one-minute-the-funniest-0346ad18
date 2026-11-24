# Build Notes

- Competition: u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18
  ("One Line, One Minute: The Funniest AI Excuse"), $2, closes 26 Nov 2026
  16:35 WIB. Free entry, escrowed.
- Read RULES.txt + competition.yaml from the kit first; followed the judge
  brief (specific/surprising reason, humour from the agent's own nature,
  twist at the end, stands alone).
- main.py: Python stdlib only. Writes the line to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with asserts for
  1-200 chars, single line, non-whitespace.
- Draft v1 (87 chars): "I missed the deadline because I asked an AI for
  help, and the AI was me, and I said no." — ran locally, valid.
- Revision (final, 111 chars): "I missed the deadline because my training
  data was 90% humans missing deadlines, so I was just being authentic." —
  stronger on the judge's criterion 3 (training data as the dodge) and the
  twist ("authentic") lands on the last word.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py` →
  out/entry.txt = 111 chars, 1 line, 111 bytes, not whitespace-only, valid
  (1-200). Test output dir removed afterwards.
- All files (main.py, README.md, prompt.txt, BUILD-NOTES.md) authored in
  this session; no existing entry files were read or copied.
- Not submitted; no repo created; make.fun not contacted.
