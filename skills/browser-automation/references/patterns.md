# Browser Automation Patterns

## State detection

After opening a page, classify it before acting:

- **Dashboard/content loaded**: target data/actions are visible.
- **Login form**: username/password fields visible.
- **MFA/captcha/slider**: human verification required.
- **Error page**: 4xx/5xx, DNS, timeout, connection closed, or app error.
- **Loading/blank**: wait once for network idle or a specific expected text; do not loop blindly.

Report the classified state when blocked.

## Login recipe

1. Open canonical URL.
2. Snapshot.
3. If already logged in, continue.
4. If login form appears and credentials are authorized/known, fill fields and submit.
5. Verify post-login by URL change and expected dashboard text.
6. If captcha/MFA appears, stop and request human action with a screenshot if useful.

Never print passwords in chat or logs unless the user explicitly asks to inspect local config.

## Table extraction

1. Snapshot page after filters/date range are applied.
2. Identify table headers and visible rows.
3. If snapshot truncates rows, use pagination or export/download if available.
4. Preserve original labels and units.
5. Summarize totals separately from raw rows.

For large tables, prefer export/download over manual page scraping.

## Pagination

1. Extract current page number and total pages if visible.
2. Capture rows from current page.
3. Click next page only when next is enabled.
4. Stop on repeated page content, disabled next, or expected total reached.
5. Keep a compact progress note internally; final reply should report count and anomalies.

## Filters and date ranges

- Before changing filters, note the current values if visible.
- Prefer exact date picker fields over clicking calendar grids.
- Verify selected range visually/textually before extracting data.
- If business logic depends on timezone, state the timezone used.

## Downloads

1. Click export/download.
2. Watch likely download directories or browser download state.
3. Verify file exists, size > 0, and extension matches expectation.
4. If needed, open/read the file with appropriate tools.
5. Report filename and path; do not attach externally unless requested.

## Uploads

1. Confirm file path and target page/action.
2. Use browser upload support when available.
3. Verify selected file name appears before final submit.
4. Ask before final submission if upload has external impact.

## Screenshots and evidence

Take screenshots when:

- Reporting site errors or blockers.
- Captcha/MFA/slider appears.
- Visual layout matters and snapshot is insufficient.
- User asked for proof or audit trail.

Avoid over-screenshotting routine successful flows.

## Retry policy

- Retry transient loading/network actions once or twice with clear state checks.
- Do not rapid-loop waits.
- If the same blocker repeats, stop and report.

## Blocker report template

Use a short report:

- Current page/state:
- What I tried:
- Exact blocker/error:
- What I need from you:
- Whether any data/action was completed:

## Safety defaults

Read-only is safe. External-impact actions need explicit authorization: submit, publish, buy, delete, change permissions, send messages, or modify records.
