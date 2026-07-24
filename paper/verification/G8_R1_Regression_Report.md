# LiteMSA-Grasp ASOC G8 R1 Regression Review

**Review date:** 2026-07-23  
**Decision:** **HOLD - G8 not closed**  
**Reviewed DOCX SHA-256:** `07727331f672c136886a682ec0aa6ac6e190e6de402ac82ed22cc5fac04da975`  
**Reviewed PDF SHA-256:** `1a40316f6bb52ba9add277f11ae642a86fd1861bc108e0221032ed1346d2ab4a`

> This review was performed by role-separated AI reviewers sharing one underlying model. Errors may be correlated. It is an internal audit, not independent human peer review, external review, credentialing, institutional endorsement, or submission authorization.

## Closed in R1

1. **Statistics:** exact p-values corrected; no-multiscale is no longer called significant; tests are labelled exploratory and unadjusted.
2. **Table 6:** rebuilt from `final_trust_aggregate.csv` only, at stored severity 3; unsupported rows removed.
3. **Reproducibility package:** Supplementary Archives S1 and S2 and exact SHA-256 register are present.
4. **Figures 3-5:** regenerated from registered frozen tables using a preserved script and hash manifest.
5. **Scope and metric wording:** targeted within-family repair, no held-out-family validation, and discrete severity-grid means are explicit.
6. **Numeric regression:** 48 of 48 checks pass.
7. **Layout/accessibility:** revised DOCX/PDF each render to 16 clean pages; accessibility audit reports zero findings.

## Remaining open P1

**G8-R1-F004 - author-owned metadata and declarations.** Author names/order, affiliations, corresponding-author details, CRediT, funding, competing interests, and acknowledgements remain placeholders. These facts cannot be inferred or invented. The supplied `Author_Metadata_and_Declarations_Form.docx` must be completed, after which the manuscript hash changes and a final G8 closure review is required.

## Current boundary

All technical/scientific P1 findings from the first G8 round are closed. The workflow remains at `hold` and must not enter G9 or external submission until the author-owned fields are completed and the new exact candidate is reviewed.
