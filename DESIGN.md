# Design System Strategy: AM Tech Digital Identity

## 1. Overview & Creative North Star
The **Creative North Star** for this design system is **"The Kinetic Luminary."** 

In the tech space, "minimalism" often defaults to a sterile, flat emptiness. This design system rejects that. We define a signature visual identity by treating the screen as a multidimensional, dark environment where light doesn't just illuminate—it defines structure. By leveraging high-contrast neon accents against a deep charcoal foundation, we create an atmosphere of precision and technological authority. 

We break the "template" look through **intentional depth layering** and **asymmetric balance**. Elements are not merely placed on a grid; they are curated within a hierarchy of light and shadow, using glassmorphism to suggest transparency and "air" within a high-density data environment.

---

## 2. Colors: Tonal Depth vs. Structural Lines
Our palette is rooted in the `background: #0a0f14`. To maintain a premium, editorial feel, we strictly adhere to specific interaction rules.

### The "No-Line" Rule
**Prohibit 1px solid borders for sectioning.** Structural separation is achieved through tonal shifts, not lines. 
- Use `surface_container_low` to define a sub-section on the main `background`.
- Use `surface_bright` to highlight active interactive zones.
- This creates a seamless, "molded" appearance rather than a boxed-in layout.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack.
1.  **Base:** `surface` (#0a0f14)
2.  **Sectioning:** `surface_container` (#141a20)
3.  **Components/Cards:** `surface_container_high` (#1a2027)
4.  **Floating Elements:** `surface_container_highest` (#1f262e) with Backdrop Blur (20px-40px).

### The "Glass & Gradient" Rule
CTAs and Hero elements must possess "soul." Use linear gradients (45-degree angle) transitioning from `primary` (#6dddff) to `primary_container` (#00d2fd). For floating navigation or side panels, use `surface_variant` at 60% opacity with a heavy blur to create a high-tech glass effect.

---

## 3. Typography: Editorial Authority
We utilize a pairing of **Manrope** for impact and **Inter** for utility.

*   **Display (Manrope):** Massive scale (`display-lg`: 3.5rem) used with tight letter-spacing (-0.02em). This conveys the "Confident and Bold" personality.
*   **Headline (Manrope):** Use `headline-lg` for section headers. These should be high-contrast (`on_surface`) to command attention.
*   **Body (Inter):** The workhorse. `body-lg` (1rem) is the standard for readability. Maintain a generous line-height (1.6) to provide the "breathing room" required for a modern tech aesthetic.
*   **Labels (Inter):** All-caps, tracked out (+0.05em) using `label-md` to denote metadata or small category tags.

---

## 4. Elevation & Depth: Atmospheric Layering
Traditional shadows are too "dirty" for this aesthetic. We use **Ambient Lighting.**

*   **The Layering Principle:** Avoid shadows for static cards. Instead, place a `surface_container_low` card on the `surface` background. The slight shift in hex code provides enough contrast for the eye to perceive depth without visual clutter.
*   **Ambient Shadows:** For elevated elements (Modals/Popovers), use a diffused shadow: `0px 24px 48px rgba(0, 0, 0, 0.4)`. To add a "tech glow," a secondary shadow of `0px 0px 12px rgba(109, 221, 255, 0.1)` (using the `primary` token) can be used to simulate light bleed.
*   **The "Ghost Border" Fallback:** If accessibility requires a container boundary, use `outline_variant` at 15% opacity. Never use 100% opaque outlines.
*   **Glassmorphism:** Use `surface_variant` with a 70% alpha channel and a `backdrop-filter: blur(12px)`. This integrates the component into the background "atmosphere."

---

## 5. Components: Precision Primitives

### Buttons
*   **Primary:** Gradient from `primary` to `primary_container`. White text (`on_primary_fixed`). Corner radius: `full` (9999px) for a high-tech, aerodynamic feel.
*   **Secondary:** `surface_bright` background with `primary` text. No border.
*   **Tertiary:** Transparent background, `primary` text, slight underline on hover.

### Cards & Lists
*   **Rule:** Forbid divider lines. 
*   **Execution:** Use 32px of vertical white space (Spacing Scale) or a subtle background shift to `surface_container_low` for every other list item to create a "zebra" effect without harsh lines.
*   **Radius:** Cards must use `xl` (1.5rem) or `lg` (1rem) corner rounding to maintain the "Soft/Clean" brand personality.

### Input Fields
*   **Base State:** `surface_container_highest` background, no border, `sm` (0.25rem) corner radius.
*   **Focus State:** A "Ghost Border" of `primary` at 40% opacity and a soft glow of 4px.
*   **Error State:** Background shifts to a very subtle tint of `error_container`.

### Additional Component: The "Data Pulse"
A small, glowing dot using `tertiary` (#b6ffed) with a CSS pulse animation. Used next to "Live" status indicators or system health metrics to reinforce the "Kinetic" nature of the system.

---

## 6. Do's and Don'ts

### Do
*   **Do** use extreme scale differences between Display and Body text to create a bold hierarchy.
*   **Do** allow elements to overlap (e.g., a card bleeding over a section break) to break the "boxed" feel.
*   **Do** use `secondary` (#b884ff) for interactive accents like hover states or progress bars to add "vibrancy."

### Don't
*   **Don't** use 1px solid black or grey borders. This instantly makes the UI look dated and "out-of-the-box."
*   **Don't** use standard "drop shadows" with high opacity. They muddy the dark theme.
*   **Don't** crowd the layout. If a section feels "busy," increase the vertical spacing by 2x. High-end tech requires "void" to feel premium.