# Python Bytes YouTube Maintenance Status

Living tracker for canonical Python Bytes YouTube metadata, safely preserved YouTube chapters, and manual English subtitles. The nightly policy inserts a unique validated managed raw-recording VTT only when no non-ASR English (`en` or `en-*`) track exists; every existing manual English track and every ASR track is preserved. Podcast-site VTT resources are never used. Unmanaged video fields are never changed.

## Run work log — 2026-07-21

- Planned allocation: up to 10 authenticated candidate slots in phase 1; unused capacity may transfer after both initial phases.
- [x] 431 — title and description updated; unique managed VTT inserted; API readback, idempotency, ASR preservation, and unmanaged-field preservation verified
- [x] 476 — title and description updated; unique managed VTT inserted; verified
- [x] 475 — title and description updated; unique managed VTT inserted; verified
- [x] 474 — title and description updated; unique managed VTT inserted; serving track verified after brief readback lag; direct-write provenance preserved
- [x] 473 — title and description updated; unique managed VTT inserted; verified
- [x] 472 — title and description updated; unique managed VTT inserted; verified
- [x] 471 — title and description updated; unique managed VTT inserted; verified
- [x] 470 — title and description updated; unique managed VTT inserted; verified
- [x] 468 — title and description updated; unique managed VTT inserted; verified; nonfatal overlap warnings recorded for cues 288, 339, and 440
- [ ] 467 — partial: title/description changed and exact metadata readback passed; caption insert was rejected by quota, idempotency not run; retry from fresh inspection

## Completed and verified episodes

- [x] 431 — title/description updated and manual English subtitles inserted; verified 2026-07-21
- [x] 480–488 — authenticated readback and idempotency verified in existing audits

## Transcript blockers

- [ ] 477 — managed VTT cue 617 has non-positive duration; repair the raw-recording WebVTT and retry
- [ ] 469 — managed VTT cue 339 has non-positive duration; repair the raw-recording WebVTT and retry

## Canonical metadata blockers

- None currently known.

## Missing mappings

- [ ] 479 — authoritative episode/video mapping returned not found; add mapping and retry
- [ ] 478 — authoritative episode/video mapping returned not found; add mapping and retry

## Quota-deferred or partial episodes

- [ ] 467 — metadata write read back exactly and unmanaged fields were unchanged; no caption write occurred because quota was exhausted; fresh inspection, caption inventory, pending insert, and idempotency are required

## Recent/new sweep

- Latest finalized mapped recording discovered: episode 488; already verified.
- Upcoming episode 489 was excluded because it is not finalized.
- No unhandled finalized mapped episode newer than 488 was found.

## Historical cursor

- Seed high-water mark: episode 488.
- Current downward cursor: episode 466; episode 467 remains the first retry because it is partial.
- Public blockers and unmapped points do not consume authenticated slots.

## Next actions

- [ ] After quota reset, reconcile episode 467 from fresh metadata/caption inspection, insert the unique managed VTT only if manual English remains absent, and verify idempotency.
- [ ] Repair the episode 477 and 469 managed VTT timing errors.
- [ ] Add mappings for episodes 479 and 478.
- [ ] Continue newest-first below the cursor on the next nightly run.

## Rollup paths

- Tonight’s reconciled rollup: `/opt/data/workspace/.hermes/youtube-sync/nightly/2026-07-21/pythonbytes-rollup.json`
- Shared nightly rollup: `/opt/data/workspace/.hermes/youtube-sync/nightly/2026-07-21/nightly-batch-rollup.json`
- Per-episode audits: `/opt/data/workspace/.hermes/youtube-sync/pythonbytes/EPISODE-VIDEO_ID/result.json`
