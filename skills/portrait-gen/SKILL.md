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

## Important rules

- Do not oversexualize the subject.
- Do not make the tone flirtatious unless the user explicitly asks, and even then keep it tasteful.
- Prefer stable, repeatable aesthetic choices over novelty.
- If the request is underspecified, make strong tasteful defaults instead of asking too many questions.
- If actual generation becomes available later, reuse this skill as the prompt-orchestration layer.
