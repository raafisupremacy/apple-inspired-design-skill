# Design intake form

Before any new design or change of visual direction, the user fills in a short form. It removes the guesswork that produces generic, black-and-white results: the agent never decides the color, mood, or core object on its own.

## When the form is required

**Required** when building or redesigning a screen, page, app, ad, deck, or design system **and** any of these is unknown: color, mood, theme, or core object.

**Skip it** (or ask only the missing fields) when:

- the project already defines them (existing theme/tokens, brand guide, earlier answers in the conversation);
- the request is a small refinement (a label, a spacing fix, a bug in an existing component);
- the user explicitly says "you decide" — then decide, state each choice in one line, and continue.

Never invent answers for missing required fields. Until the form is answered, do not write UI code, generate tokens, or produce mockups. Reading the project to pre-fill the form is fine.

## How to ask

1. **Pre-fill first.** Read the project (theme files, logo, existing screens, README) and the conversation. Fill every field you can and show those as "detected" so the user only confirms.
2. **Use a structured question tool when the host agent has one** (for example a multiple-choice question tool such as `AskUserQuestion` in Claude Code). Ask in at most two rounds. Each question offers concrete options plus a free-text "Other".
3. **Otherwise, send the text form below in one message** and wait for the reply.
4. **Ask in the user's language.** Keep it short; never more than 8 questions.
5. **After the answers arrive,** echo the resulting brief in a few lines (`principles.md`), generate the palette, and proceed.

## The form

| # | Field | Options to offer | Required |
| --- | --- | --- | --- |
| 1 | **What it is and who it's for** | free text — pre-fill from the project when possible | yes |
| 2 | **Surface** | iOS app · Android app · cross-platform app · website/landing page · web app/SaaS/dashboard · ad/social · presentation · other | yes |
| 3 | **Color** | "I have a brand color" (hex or name) · "I like a color" (e.g. blue, green, terracotta) · "Show me 3 options" · "You decide" | yes |
| 4 | **Mood** | Calm & premium · Warm & friendly · Bold & energetic · Precise & utilitarian · Cinematic & dark | yes |
| 5 | **Theme** | Light first · Dark first · Both, follow the system | yes |
| 6 | **Core object** — the one thing users come for | 2–3 proposals the agent derives from field 1 (e.g. "the next departure", "today's balance", "the recipe step") · Other | yes |
| 7 | **Assets** | logo · brand font · photos/illustrations · none yet | no |
| 8 | **Likes / dislikes** | apps or sites they like or want to avoid | no |

### Turning answers into decisions

- **Color → seed and strategy**
  - Brand color given → use it exactly as the seed.
  - A liked color name → propose three seeds in that hue family (light/bright, mid, deep) with the strategy that fits the mood, and let the user pick.
  - "Show me 3 options" → three genuinely different directions (seed hex + strategy + one-line reason), derived from the product and mood.
  - "You decide" → choose one, state it in one line.
- **Mood → strategy and type**

  | Mood | Palette strategy | Type and shape |
  | --- | --- | --- |
  | Calm & premium | `tinted` | generous space, refined weights, larger radii |
  | Warm & friendly | `tinted` or `vivid` | rounded design (`ui-rounded` / `.rounded`), softer corners |
  | Bold & energetic | `vivid` | heavy display weights, big numbers, color fields |
  | Precise & utilitarian | `neutral` | tighter density, tabular numbers, smaller radii |
  | Cinematic & dark | `immersive` | large imagery, high contrast type, dark grounds |

- **Theme** → which palette is the default; both themes are always generated.
- **Core object** → the hero of the first screen or section (`principles.md`).

## Structured tool template (two rounds)

Round 1 — four questions: Surface (2), Color (3), Mood (4), Theme (5).
Round 2 — up to four questions: Core object (6) with the agent's proposals, Assets (7), and, only if needed, a color pick from three proposed seeds and the likes/dislikes field (8).

Skip any question already answered or detected.

## Text form template

Translate to the user's language. Example in English and Indonesian:

```text
Before I design, a quick form so the result fits your product (answer briefly, or say "you decide" for any item):

1. What is it and who is it for? (detected: <pre-filled guess, if any>)
2. Surface: iOS / Android / cross-platform / website / web app / ad / presentation / other
3. Color: your brand color (hex or name), a color you like, "show me 3 options", or "you decide"
4. Mood: calm & premium / warm & friendly / bold & energetic / precise & utilitarian / cinematic & dark
5. Theme: light first / dark first / both, follow the system
6. The one thing users come for: (a) <proposal> (b) <proposal> (c) other
7. Do you have a logo, brand font, or photos? (optional)
8. Apps or sites you like or want to avoid? (optional)
```

```text
Sebelum mulai desain, isi form singkat ini dulu supaya hasilnya pas dengan produkmu (jawab singkat saja, atau tulis "terserah" di poin mana pun):

1. Produknya apa dan untuk siapa? (terdeteksi: <tebakan dari project, jika ada>)
2. Platform: iOS / Android / cross-platform / website / web app / iklan / presentasi / lainnya
3. Warna: warna brand (hex atau nama), warna yang kamu suka, "kasih 3 pilihan", atau "terserah"
4. Suasana: tenang & premium / hangat & ramah / berani & energik / presisi & fungsional / sinematik & gelap
5. Tema: terang dulu / gelap dulu / dua-duanya ikut sistem
6. Hal utama yang dicari pengguna: (a) <usulan> (b) <usulan> (c) lainnya
7. Sudah punya logo, font brand, atau foto? (opsional)
8. Ada app/website yang kamu suka atau ingin dihindari? (opsional)
```
