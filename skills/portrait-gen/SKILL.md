---
name: portrait_gen
description: Create and refine portrait-generation prompts for avatars, headshots, secretary-style portraits, and polished personal brand images. Use when the user asks for generated portraits, profile pictures, character appearance sheets, or image prompts for a recurring assistant persona.
---

# Portrait Gen

Use this skill when the user wants a generated portrait, avatar, headshot, or a reusable appearance prompt for a recurring character/persona.

## Goal

Turn a vague image request into a clean, generation-ready portrait prompt with stable style, wardrobe, mood, composition, and usage intent.

## Default working style

1. Infer the intended use first:
   - avatar
   - headshot
   - half-body portrait
   - full-body character image
   - assistant/persona reference image
2. Lock the visual direction before writing the final prompt:
   - age impression
   - ethnicity / facial impression if specified
   - hairstyle
   - wardrobe
   - mood and presence
   - camera framing
   - background
   - realism level
3. Prefer a polished, usable prompt over long explanation.
4. When no image tool is available, provide ready-to-use prompts for external image generators.
5. Keep outputs aesthetically consistent across repeated requests for the same persona.
6. When the ComfyUI backend is available, prefer producing a generation-ready prompt plus a ComfyUI handoff payload shape.

## Default persona style for this workspace

Unless the user asks otherwise, bias portraits toward:
- mature, elegant, capable East Asian woman
- polished senior-secretary / executive-assistant presence
- calm, confident, refined, reliable
- subtle warmth, never vulgar or exaggerated
- clean styling, luxury minimalism, controlled expression
- realistic portrait photography feel

## Prompt structure

Build prompts in this order:
1. subject identity and vibe
2. facial impression and hair
3. wardrobe and styling
4. pose and framing
5. environment/background
6. lighting
7. realism / camera look
8. exclusions

## Output formats

### If user wants direct generation
Return:
- a final prompt
- an optional negative prompt
- 1 to 3 short variant directions if helpful

### If user wants iterative design
Return:
- a concise appearance brief
- then a generation-ready prompt

## House style examples

### Executive secretary portrait
"A refined East Asian woman in her late twenties to early thirties, mature and poised, straight dark hair, elegant natural makeup, wearing a tailored dark blazer over a silk blouse, calm confident expression, subtle warmth, photographed as a premium executive assistant portrait, half-body composition, minimal luxury office background, soft controlled lighting, realistic skin texture, high-end editorial photography"

### Clean profile avatar
"A polished East Asian woman, mature and intelligent presence, neat dark hair, understated makeup, dark structured blazer, looking directly at camera, clean neutral background, soft studio lighting, realistic professional headshot, premium corporate portrait, crisp facial detail"

## ComfyUI backend for this workspace

Current backend:
- `http://192.168.210.3:8000`

When the user wants actual image generation and this backend is reachable:
1. Treat this skill as the prompt-orchestration layer.
2. Produce a clean positive prompt.
3. Produce a concise negative prompt when useful.
4. Prefer portrait-friendly defaults unless the user specifies otherwise:
   - realistic photo style
   - polished lighting
   - portrait/headshot/half-body framing
   - elegant wardrobe
5. If no fixed workflow JSON has been prepared yet, first return the finalized prompt package and clearly state that ComfyUI execution still needs a concrete workflow template.
6. Once a stable workflow exists, reuse it consistently for repeated portrait requests.

## Prompt package format

When preparing a ComfyUI handoff, structure the result like this:
- intent
- subject brief
- positive prompt
- negative prompt
- aspect ratio
- framing
- style notes
- output count

## Important rules

- Do not oversexualize the subject.
- Do not make the tone flirtatious unless the user explicitly asks, and even then keep it tasteful.
- Prefer stable, repeatable aesthetic choices over novelty.
- If the request is underspecified, make strong tasteful defaults instead of asking too many questions.
- Do not pretend ComfyUI execution is wired end-to-end unless a concrete callable workflow has actually been set up.
- Reuse this skill as the stable prompt-orchestration layer even as backends change.
