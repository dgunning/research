# SecFlow Design Agency - UX Design Guide

## Design Philosophy

SecFlow Design's visual identity embodies the intersection of sophisticated financial services, cutting-edge AI technology, and elegant technical excellence. The design language is **post-SaaS**: moving beyond the generic blue-gradient SaaS aesthetic toward something more refined, intelligent, and purposefully technical.

### Core Design Principles

1. **Intelligent Simplicity** - Complex systems made comprehensible through thoughtful design
2. **Technical Elegance** - Beauty in precision, not decoration
3. **Trustworthy Modernism** - Forward-thinking but stable and professional
4. **Data-Informed Aesthetics** - Visual language that speaks to both technical and business audiences
5. **AI-Native Design** - Design that suggests intelligence without being overtly "robot-y"

### Brand Positioning Through Design

**We Are:**
- Sophisticated, not flashy
- Technical, not academic
- Modern, not trendy
- Intelligent, not complex
- Premium, not expensive-looking

**We Are Not:**
- Generic blue SaaS gradient
- Overly corporate/stuffy
- Playful/casual startup
- Minimalist to the point of emptiness
- Flashy fintech neon

---

## Visual Identity

### Brand Essence

**Archetype:** The Expert Guide
**Personality:** Intelligent, precise, trustworthy, forward-thinking, sophisticated
**Voice:** Confident but approachable, technical but clear
**Emotion:** Calm confidence, intellectual curiosity, strategic clarity

### Design Metaphors

Our visual language draws from:
1. **Financial Markets** - Precision, data, signals, patterns
2. **AI/ML Systems** - Networks, nodes, intelligence, automation
3. **Architecture** - Structure, space, precision, elegance
4. **Data Visualization** - Clarity, insight, patterns emerging from complexity

---

## Color System

### Primary Palette

Our color system is built around a sophisticated neutral base with accent colors that suggest intelligence and precision.

#### Brand Colors

**Obsidian (Primary Dark)**
- Hex: `#0A0E1A`
- RGB: `10, 14, 26`
- Usage: Primary backgrounds, headers, dark mode base
- Psychology: Deep, sophisticated, technical depth

**Slate (Secondary Dark)**
- Hex: `#1A1F2E`
- RGB: `26, 31, 46`
- Usage: Cards, panels, secondary backgrounds
- Psychology: Professional, grounded, stable

**Graphite (Tertiary Dark)**
- Hex: `#2A2F3E`
- RGB: `42, 47, 62`
- Usage: Borders, dividers, subtle elements
- Psychology: Refined, technical, modern

#### Accent Colors

**Electric Teal (Primary Accent)**
- Hex: `#00D9D9`
- RGB: `0, 217, 217`
- Usage: Primary CTAs, interactive elements, highlights
- Psychology: Intelligent, precise, forward-thinking
- Technical note: High contrast against dark backgrounds
- AI association: Suggests computational intelligence without cliché

**Quantum Violet (Secondary Accent)**
- Hex: `#8B5CF6`
- RGB: `139, 92, 246`
- Usage: Secondary actions, agent indicators, AI features
- Psychology: Innovation, intelligence, premium
- AI association: Deep learning, neural networks

**Signal Green (Success/Data)**
- Hex: `#10B981`
- RGB: `16, 185, 129`
- Usage: Success states, positive data, validation
- Psychology: Confirmation, growth, positive outcomes

**Amber Alert (Warning/Attention)**
- Hex: `#F59E0B`
- RGB: `245, 158, 11`
- Usage: Warnings, important information, highlights
- Psychology: Attention without alarm

**Critical Red (Error/Urgent)**
- Hex: `#EF4444`
- RGB: `239, 68, 68`
- Usage: Errors, urgent actions, destructive operations
- Psychology: Clear, immediate, requires attention

#### Neutral Palette

**Ghost White (Primary Light)**
- Hex: `#F8F9FA`
- RGB: `248, 249, 250`
- Usage: Light mode backgrounds, content areas
- Psychology: Clean, spacious, professional

**Cloud Gray (Secondary Light)**
- Hex: `#E5E7EB`
- RGB: `229, 231, 235`
- Usage: Light mode dividers, subtle backgrounds
- Psychology: Soft, organized, clear

**Steel (Mid Tone)**
- Hex: `#64748B`
- RGB: `100, 116, 139`
- Usage: Secondary text, icons, placeholders
- Psychology: Balanced, readable, professional

**Charcoal (Primary Text on Light)**
- Hex: `#1E293B`
- RGB: `30, 41, 59`
- Usage: Primary text on light backgrounds
- Psychology: Readable, authoritative, clear

**Platinum (Primary Text on Dark)**
- Hex: `#F1F5F9`
- RGB: `241, 245, 249`
- Usage: Primary text on dark backgrounds
- Psychology: Clear, readable, modern

### Color Usage Guidelines

#### Backgrounds

**Dark Mode (Recommended Default):**
```
Primary: Obsidian (#0A0E1A)
Secondary: Slate (#1A1F2E)
Tertiary: Graphite (#2A2F3E)
```

**Light Mode:**
```
Primary: Ghost White (#F8F9FA)
Secondary: Cloud Gray (#E5E7EB)
Tertiary: White (#FFFFFF)
```

#### Interactive Elements

**Primary Actions:**
- Background: Electric Teal (#00D9D9)
- Text: Obsidian (#0A0E1A)
- Hover: Brighter variant (#00F5F5)
- Active: Darker variant (#00B8B8)

**Secondary Actions:**
- Background: Transparent
- Border: Electric Teal (#00D9D9)
- Text: Electric Teal (#00D9D9)
- Hover: Background at 10% opacity

**AI/Agent Features:**
- Accent: Quantum Violet (#8B5CF6)
- Glow: Soft violet shadow
- Indicator: Pulsing violet dot

#### Data Visualization

**Sequential Data (Light to Dark):**
```
#E0F2FE → #7DD3FC → #0EA5E9 → #0369A1 → #0C4A6E
```

**Diverging Data (Negative to Positive):**
```
#EF4444 → #F59E0B → #F3F4F6 → #10B981 → #059669
```

**Categorical Data:**
```
Electric Teal, Quantum Violet, Signal Green, Amber Alert,
Coral (#FF6B6B), Sky (#3B82F6), Emerald (#34D399)
```

### Accessibility

All color combinations meet WCAG 2.1 AA standards minimum (AAA preferred):

**Text Contrast Ratios:**
- Primary text on dark: 15.8:1 (AAA)
- Primary text on light: 12.6:1 (AAA)
- Electric Teal on dark: 5.8:1 (AA Large)
- Quantum Violet on dark: 7.2:1 (AA)

---

## Typography

### Font System

Our typography system balances technical precision with elegant readability.

#### Primary Font: Inter

**Why Inter:**
- Designed for screens and interfaces
- Excellent readability at all sizes
- Professional yet modern
- Open source (free, aligns with edgartools ethos)
- Extensive weight range
- Superior legibility in technical contexts

**Weights Used:**
- Light (300): Subtext, captions, less emphasis
- Regular (400): Body text, standard content
- Medium (500): Emphasized text, labels
- Semibold (600): Subheadings, section titles
- Bold (700): Headings, strong emphasis

**Font Stack:**
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont,
             'Segoe UI', 'Roboto', 'Helvetica Neue', Arial,
             sans-serif;
```

#### Monospace Font: JetBrains Mono

**Why JetBrains Mono:**
- Designed for developers
- Excellent for code display
- Clear character differentiation (0 vs O, 1 vs l)
- Supports ligatures
- Free and open source

**Usage:**
- Code snippets
- Technical data
- API responses
- File paths
- Terminal output

**Font Stack:**
```css
font-family: 'JetBrains Monospace', 'Fira Code', 'Monaco',
             'Courier New', monospace;
```

### Type Scale

**Desktop Scale (1.250 - Major Third):**
```
Hero/H1:     48px / 3rem      (Bold, -1% tracking)
H2:          38px / 2.375rem  (Semibold, -0.5% tracking)
H3:          30px / 1.875rem  (Semibold, 0% tracking)
H4:          24px / 1.5rem    (Semibold, 0% tracking)
H5:          20px / 1.25rem   (Medium, 0% tracking)
Body Large:  18px / 1.125rem  (Regular, 0% tracking)
Body:        16px / 1rem      (Regular, 0% tracking)
Body Small:  14px / 0.875rem  (Regular, 0.5% tracking)
Caption:     12px / 0.75rem   (Regular, 1% tracking)
Micro:       10px / 0.625rem  (Medium, 1.5% tracking)
```

**Mobile Scale (1.200 - Minor Third):**
```
Hero/H1:     36px / 2.25rem   (Bold, -1% tracking)
H2:          30px / 1.875rem  (Semibold, -0.5% tracking)
H3:          25px / 1.563rem  (Semibold, 0% tracking)
H4:          21px / 1.313rem  (Semibold, 0% tracking)
H5:          18px / 1.125rem  (Medium, 0% tracking)
Body Large:  16px / 1rem      (Regular, 0% tracking)
Body:        15px / 0.938rem  (Regular, 0% tracking)
Body Small:  13px / 0.813rem  (Regular, 0.5% tracking)
Caption:     12px / 0.75rem   (Regular, 1% tracking)
Micro:       10px / 0.625rem  (Medium, 1.5% tracking)
```

### Line Height

```
Headings (H1-H3):   1.2 (tight, strong presence)
Subheadings (H4-H5): 1.3 (slightly more breathing room)
Body text:          1.6 (optimal readability)
Captions:           1.4 (compact but readable)
Code:               1.5 (technical readability)
```

### Typography Guidelines

#### Headings

**Usage:**
- H1: Page titles, hero sections (one per page)
- H2: Major section headings
- H3: Subsection headings
- H4: Component/card titles
- H5: Small section labels

**Style:**
- Always sentence case (except proper nouns)
- No periods at end
- Maintain hierarchy (don't skip levels)
- Dark mode: Platinum color
- Light mode: Charcoal color

#### Body Text

**Paragraph Spacing:**
- Between paragraphs: 1.5em
- After headings: 0.75em
- Before headings: 2em

**Line Length:**
- Optimal: 60-75 characters
- Maximum: 85 characters
- Blog posts: 65 characters ideal

**Link Styling:**
- Color: Electric Teal
- Underline on hover
- No underline in body (unless ambiguous)
- Always underlined in footer/navigation

#### Code & Technical Text

**Inline Code:**
```css
background: rgba(0, 217, 217, 0.1);
color: Electric Teal;
padding: 2px 6px;
border-radius: 4px;
font-size: 0.9em;
```

**Code Blocks:**
```css
background: Slate (#1A1F2E);
border: 1px solid Graphite (#2A2F3E);
border-radius: 8px;
padding: 20px;
font-size: 14px;
line-height: 1.5;
```

**Syntax Highlighting Theme:**
- Base: "Night Owl" style (Sarah Drasner)
- Modified colors to match brand palette
- Teal for functions, Violet for keywords

---

## Layout & Spacing

### Grid System

**12-Column Grid:**
- Desktop: 1440px max width, 80px margins, 24px gutters
- Tablet: 768px max width, 40px margins, 20px gutters
- Mobile: 375px base, 20px margins, 16px gutters

**Container Widths:**
```
XL Container: 1280px (marketing pages)
Large Container: 1024px (blog posts, documentation)
Medium Container: 768px (forms, focused content)
Small Container: 640px (narrow reading)
```

### Spacing Scale (8px Base)

**Base Unit: 8px**

```
XXS:  4px   (0.25rem) - Tight spacing, icon padding
XS:   8px   (0.5rem)  - Button padding, small gaps
SM:   12px  (0.75rem) - Compact lists, tight sections
MD:   16px  (1rem)    - Standard spacing, card padding
LG:   24px  (1.5rem)  - Section spacing, card gaps
XL:   32px  (2rem)    - Large section gaps
2XL:  48px  (3rem)    - Major section dividers
3XL:  64px  (4rem)    - Hero spacing, page sections
4XL:  96px  (6rem)    - Hero sections, page headers
5XL:  128px (8rem)    - Extreme spacing, landing pages
```

### Breakpoints

```css
/* Mobile first approach */
sm:  640px   /* Small devices */
md:  768px   /* Tablets */
lg:  1024px  /* Laptops */
xl:  1280px  /* Desktops */
2xl: 1536px  /* Large screens */
```

### Layout Patterns

#### Hero Section
```
Height: 60-80vh (viewport height)
Padding: 5XL top, 4XL bottom
Content: Center-aligned or left-aligned
Max-width: XL Container
Background: Subtle gradient or pattern
```

#### Content Sections
```
Padding: 3XL top and bottom (desktop)
Padding: 2XL top and bottom (mobile)
Gap between sections: 4XL
Max-width: Large or XL Container
```

#### Cards
```
Padding: LG to XL
Border-radius: 12px (modern, not too round)
Border: 1px solid (subtle)
Shadow: Soft, elevated on hover
Gap between cards: LG
```

#### Forms
```
Max-width: Medium Container
Field spacing: MD
Section spacing: XL
Label to input: XS
Helper text: XS below input
```

---

## Visual Style

### Borders & Corners

**Border Radius:**
```
Small:  4px  - Buttons, tags, badges
Medium: 8px  - Inputs, small cards
Large:  12px - Cards, modals, containers
XLarge: 16px - Hero cards, feature blocks
Round:  9999px - Pills, avatars, status dots
```

**Border Widths:**
```
Thin:    1px  - Standard borders, dividers
Medium:  2px  - Focus states, emphasis
Thick:   3px  - Strong emphasis, brand elements
```

**Border Style:**
- Default: Solid
- Interactive elements: May use gradient borders
- Focus states: Always solid, high contrast

### Shadows & Elevation

**Shadow Scale (Subtle, Modern):**

```css
/* No shadow - flat elements */
none: box-shadow: none;

/* SM - Slight lift, subtle cards */
sm: box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);

/* MD - Standard cards, dropdowns */
md: box-shadow:
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);

/* LG - Modals, popovers, emphasized cards */
lg: box-shadow:
    0 10px 15px -3px rgba(0, 0, 0, 0.1),
    0 4px 6px -2px rgba(0, 0, 0, 0.05);

/* XL - Drawers, major modals */
xl: box-shadow:
    0 20px 25px -5px rgba(0, 0, 0, 0.1),
    0 10px 10px -5px rgba(0, 0, 0, 0.04);

/* 2XL - Maximum elevation */
2xl: box-shadow:
    0 25px 50px -12px rgba(0, 0, 0, 0.25);

/* Glow - AI/Interactive elements */
glow-teal: box-shadow:
    0 0 20px rgba(0, 217, 217, 0.3),
    0 0 40px rgba(0, 217, 217, 0.1);

glow-violet: box-shadow:
    0 0 20px rgba(139, 92, 246, 0.3),
    0 0 40px rgba(139, 92, 246, 0.1);
```

**Elevation Hierarchy:**
1. Base layer (no shadow)
2. Flat elements (no shadow)
3. Cards and panels (sm shadow)
4. Interactive elements (md shadow, lg on hover)
5. Modals and overlays (xl or 2xl shadow)
6. AI/Special features (glow effect)

### Backgrounds

#### Solid Backgrounds

**Dark Mode:**
- Primary: Obsidian
- Secondary: Slate
- Tertiary: Graphite

**Light Mode:**
- Primary: Ghost White
- Secondary: White
- Tertiary: Cloud Gray

#### Gradient Backgrounds

**Subtle Hero Gradient (Dark):**
```css
background: linear-gradient(
    135deg,
    #0A0E1A 0%,
    #1A1F2E 50%,
    #0A0E1A 100%
);
```

**Accent Gradient (Teal to Violet):**
```css
background: linear-gradient(
    135deg,
    #00D9D9 0%,
    #8B5CF6 100%
);
```

**Data Visualization Gradient:**
```css
background: linear-gradient(
    90deg,
    #00D9D9 0%,
    #10B981 100%
);
```

#### Pattern Backgrounds

**Subtle Grid (Technical Feel):**
```css
background-image:
    linear-gradient(rgba(0, 217, 217, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 217, 217, 0.03) 1px, transparent 1px);
background-size: 50px 50px;
```

**Dot Pattern (Modern, Minimal):**
```css
background-image:
    radial-gradient(rgba(0, 217, 217, 0.1) 1px, transparent 1px);
background-size: 20px 20px;
```

**Noise Texture (Subtle Depth):**
```css
background-image: url('/textures/noise.png');
opacity: 0.03;
mix-blend-mode: overlay;
```

### Opacity Scale

```css
0:    0     - Completely transparent
5:    0.05  - Barely visible
10:   0.1   - Very subtle
20:   0.2   - Subtle overlays
30:   0.3   - Visible overlays
40:   0.4   - Disabled states
50:   0.5   - Moderate transparency
60:   0.6   - Emphasized transparency
70:   0.7   - Mostly visible
80:   0.8   - Very visible
90:   0.9   - Nearly opaque
95:   0.95  - Almost solid
100:  1     - Completely opaque
```

---

## Components

### Buttons

#### Primary Button
```css
background: Electric Teal;
color: Obsidian;
padding: 12px 24px;
border-radius: 8px;
font-weight: 600;
font-size: 16px;
letter-spacing: -0.01em;
transition: all 150ms ease;

hover:
  background: #00F5F5;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 217, 217, 0.3);

active:
  background: #00B8B8;
  transform: translateY(0);
```

**Sizes:**
- Small: 8px 16px, 14px font
- Medium: 12px 24px, 16px font
- Large: 16px 32px, 18px font

#### Secondary Button
```css
background: transparent;
color: Electric Teal;
border: 2px solid Electric Teal;
padding: 10px 22px; /* Adjust for border */
border-radius: 8px;
font-weight: 600;

hover:
  background: rgba(0, 217, 217, 0.1);
  border-color: #00F5F5;
```

#### Ghost Button
```css
background: transparent;
color: Platinum;
padding: 12px 24px;
border-radius: 8px;
font-weight: 500;

hover:
  background: rgba(241, 245, 249, 0.1);
```

#### AI Feature Button (Special)
```css
background: linear-gradient(135deg, #00D9D9, #8B5CF6);
color: white;
padding: 12px 24px;
border-radius: 8px;
font-weight: 600;
position: relative;

hover:
  box-shadow: 0 0 20px rgba(139, 92, 246, 0.4);

/* Animated gradient on hover */
background-size: 200% 200%;
animation: gradient-shift 3s ease infinite;
```

### Input Fields

```css
background: rgba(241, 245, 249, 0.05);
border: 1px solid Graphite;
border-radius: 8px;
padding: 12px 16px;
color: Platinum;
font-size: 16px;
transition: all 200ms ease;

placeholder:
  color: Steel;
  opacity: 0.6;

focus:
  border-color: Electric Teal;
  box-shadow: 0 0 0 3px rgba(0, 217, 217, 0.1);
  outline: none;

error:
  border-color: Critical Red;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
```

**Field Variants:**
- Text input
- Textarea (same styling)
- Select dropdown (custom arrow)
- Checkbox (custom design)
- Radio button (custom design)
- Toggle switch (teal accent)

### Cards

#### Standard Card
```css
background: Slate;
border: 1px solid Graphite;
border-radius: 12px;
padding: 24px;
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
transition: all 200ms ease;

hover:
  border-color: rgba(0, 217, 217, 0.3);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
```

#### Feature Card (Emphasized)
```css
background: linear-gradient(
    135deg,
    rgba(0, 217, 217, 0.05),
    rgba(139, 92, 246, 0.05)
);
border: 1px solid rgba(0, 217, 217, 0.2);
border-radius: 12px;
padding: 32px;
position: relative;

/* Accent line */
::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #00D9D9, #8B5CF6);
}
```

#### Interactive Card (Clickable)
```css
cursor: pointer;
transition: all 150ms ease;

hover:
  transform: translateY(-4px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);

active:
  transform: translateY(-2px);
```

### Badges & Tags

```css
/* Status Badge */
display: inline-flex;
align-items: center;
padding: 4px 12px;
border-radius: 9999px;
font-size: 12px;
font-weight: 600;
letter-spacing: 0.5px;
text-transform: uppercase;

/* Success */
background: rgba(16, 185, 129, 0.1);
color: Signal Green;

/* Warning */
background: rgba(245, 158, 11, 0.1);
color: Amber Alert;

/* Error */
background: rgba(239, 68, 68, 0.1);
color: Critical Red;

/* AI Feature Tag */
background: linear-gradient(135deg,
    rgba(0, 217, 217, 0.2),
    rgba(139, 92, 246, 0.2));
color: Quantum Violet;
```

### Navigation

#### Top Navigation Bar
```css
background: rgba(10, 14, 26, 0.8);
backdrop-filter: blur(12px);
border-bottom: 1px solid Graphite;
padding: 16px 32px;
position: sticky;
top: 0;
z-index: 50;

/* Logo area */
height: 64px;
```

**Nav Links:**
```css
color: Platinum;
font-weight: 500;
font-size: 15px;
padding: 8px 16px;
border-radius: 6px;
transition: all 150ms ease;

hover:
  background: rgba(241, 245, 249, 0.1);
  color: Electric Teal;

active:
  background: rgba(0, 217, 217, 0.1);
  color: Electric Teal;
```

### Modals & Overlays

```css
/* Overlay backdrop */
background: rgba(10, 14, 26, 0.8);
backdrop-filter: blur(8px);

/* Modal container */
background: Slate;
border: 1px solid Graphite;
border-radius: 16px;
box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
max-width: 600px;
padding: 32px;

/* Modal header */
border-bottom: 1px solid Graphite;
padding-bottom: 16px;
margin-bottom: 24px;
```

### Loading States

**Spinner:**
```css
/* Animated teal spinner */
border: 3px solid rgba(0, 217, 217, 0.1);
border-top-color: Electric Teal;
border-radius: 50%;
animation: spin 1s linear infinite;
```

**Skeleton Loader:**
```css
background: linear-gradient(
    90deg,
    rgba(42, 47, 62, 0.4) 0%,
    rgba(42, 47, 62, 0.6) 50%,
    rgba(42, 47, 62, 0.4) 100%
);
background-size: 200% 100%;
animation: shimmer 1.5s infinite;
border-radius: 8px;
```

**Progress Bar:**
```css
background: Graphite;
height: 4px;
border-radius: 2px;
overflow: hidden;

/* Fill */
background: linear-gradient(90deg, #00D9D9, #8B5CF6);
height: 100%;
transition: width 300ms ease;
```

---

## Iconography

### Icon System

**Primary Icon Set: Lucide Icons**
- Consistent style
- Open source
- Comprehensive library
- 24x24 base size
- Customizable stroke width

**Icon Sizes:**
```
XS:  12px - Inline indicators
SM:  16px - Text inline, small buttons
MD:  20px - Standard buttons, navigation
LG:  24px - Default size, feature highlights
XL:  32px - Section headers
2XL: 48px - Hero sections, empty states
3XL: 64px - Large illustrations
```

**Icon Stroke Width:**
- Thin: 1.5px (elegant, minimal)
- Regular: 2px (standard)
- Bold: 2.5px (emphasis)

### Icon Usage

**Interactive Icons:**
```css
color: Platinum;
cursor: pointer;
transition: all 150ms ease;

hover:
  color: Electric Teal;
  transform: scale(1.1);

active:
  transform: scale(0.95);
```

**Status Icons:**
- Success: Check circle (Signal Green)
- Warning: Alert triangle (Amber Alert)
- Error: X circle (Critical Red)
- Info: Info circle (Electric Teal)
- AI: Sparkles or network (Quantum Violet)

**Navigation Icons:**
- Use consistently across interface
- Always align with text baseline
- 16px size inline with text
- 20-24px size in navigation

### Custom Icons & Illustrations

**Style Guidelines:**
- Geometric, minimal
- Consistent stroke width (2px)
- Rounded corners (match border radius)
- Monochrome or duo-tone (Teal + Violet)
- Technical feel (grid-based, precise)

**Illustration Style:**
- Isometric or flat 2.5D
- Limited color palette (brand colors only)
- Subtle gradients acceptable
- Avoid photorealism
- Suggest intelligence/automation through visual metaphors

---

## Motion & Animation

### Animation Principles

1. **Purposeful** - Every animation serves a function
2. **Subtle** - Never distracting or excessive
3. **Fast** - Quick transitions (150-300ms)
4. **Natural** - Easing that feels organic
5. **Consistent** - Same patterns throughout

### Timing & Easing

**Durations:**
```
Instant:  50ms   - Hover state changes
Fast:     150ms  - Standard transitions
Normal:   200ms  - Modal open/close
Slow:     300ms  - Page transitions
Deliberate: 500ms - Special animations
```

**Easing Functions:**
```css
/* Default - smooth and natural */
ease-out: cubic-bezier(0.4, 0, 0.2, 1);

/* Snappy - quick and responsive */
ease-in-out: cubic-bezier(0.4, 0, 0.6, 1);

/* Bounce - playful (use sparingly) */
bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);

/* Elastic - special moments only */
elastic: cubic-bezier(0.175, 0.885, 0.32, 1.275);
```

### Common Animations

**Fade In:**
```css
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
animation: fadeIn 200ms ease-out;
```

**Slide Up:**
```css
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
animation: slideUp 300ms ease-out;
```

**Scale In (Modals):**
```css
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
animation: scaleIn 200ms ease-out;
```

**Shimmer (Loading):**
```css
@keyframes shimmer {
  from {
    background-position: -200% 0;
  }
  to {
    background-position: 200% 0;
  }
}
animation: shimmer 1.5s infinite;
```

**Glow Pulse (AI Elements):**
```css
@keyframes glowPulse {
  0%, 100% {
    box-shadow: 0 0 20px rgba(0, 217, 217, 0.3);
  }
  50% {
    box-shadow: 0 0 30px rgba(0, 217, 217, 0.5);
  }
}
animation: glowPulse 2s ease-in-out infinite;
```

**Gradient Shift (Premium Buttons):**
```css
@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
animation: gradientShift 3s ease infinite;
```

### Interaction Patterns

**Button Click:**
```css
active {
  transform: scale(0.98);
  transition: transform 50ms ease;
}
```

**Card Hover:**
```css
hover {
  transform: translateY(-4px);
  transition: transform 200ms ease-out;
}
```

**Link Underline:**
```css
text-decoration: none;
position: relative;

::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: Electric Teal;
  transition: width 200ms ease-out;
}

hover::after {
  width: 100%;
}
```

### Micro-interactions

**Success Confirmation:**
- Checkmark icon scales in
- Brief green glow
- Fade out after 2s

**Form Field Focus:**
- Border color shift
- Shadow grows
- Label moves up (if floating)

**AI Processing Indicator:**
- Pulsing violet dot
- Subtle glow
- Optional rotating spinner

---

## Data Visualization

### Chart Styling

**General Principles:**
- Clean, minimal axes
- Subtle grid lines (opacity 0.1)
- Bold data (the hero)
- Contextual colors (meaning-driven)
- Interactive tooltips

**Colors:**
- Use brand palette first
- Sequential: Teal gradient
- Diverging: Red → Gray → Green
- Categorical: Full palette rotation

**Tooltip Style:**
```css
background: Slate;
border: 1px solid Graphite;
border-radius: 8px;
padding: 12px;
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
font-size: 14px;
```

### Data Tables

```css
/* Table container */
border: 1px solid Graphite;
border-radius: 12px;
overflow: hidden;

/* Header row */
background: rgba(0, 217, 217, 0.05);
border-bottom: 2px solid Electric Teal;
font-weight: 600;
padding: 16px;

/* Body rows */
border-bottom: 1px solid Graphite;
padding: 16px;
transition: background 150ms ease;

hover:
  background: rgba(241, 245, 249, 0.03);

/* Alternating rows (optional) */
nth-child(even):
  background: rgba(241, 245, 249, 0.02);
```

### Metrics Display

**Stat Card:**
```css
background: Slate;
border: 1px solid Graphite;
border-radius: 12px;
padding: 24px;

/* Large number */
font-size: 48px;
font-weight: 700;
color: Electric Teal;
line-height: 1;

/* Label */
font-size: 14px;
color: Steel;
text-transform: uppercase;
letter-spacing: 1px;
margin-bottom: 8px;

/* Trend indicator */
display: flex;
align-items: center;
gap: 4px;
color: Signal Green; /* or Critical Red */
font-size: 14px;
font-weight: 600;
```

---

## Accessibility

### WCAG 2.1 AA Compliance (Minimum)

**Color Contrast:**
- Normal text: 4.5:1 minimum
- Large text (18px+): 3:1 minimum
- Target: AAA (7:1 for normal, 4.5:1 for large)

**Interactive Elements:**
- Minimum touch target: 44x44px
- Visual focus indicator on all interactive elements
- Focus order follows logical reading order

**Keyboard Navigation:**
- All functionality available via keyboard
- Tab order is logical and predictable
- Skip links for main content
- Focus trap in modals

**Screen Readers:**
- Semantic HTML (nav, main, article, aside)
- ARIA labels where needed
- Alt text for all images
- Live regions for dynamic content

### Focus States

```css
/* Default focus ring (override browser) */
:focus {
  outline: 2px solid Electric Teal;
  outline-offset: 2px;
}

/* Focus visible (keyboard only) */
:focus-visible {
  outline: 2px solid Electric Teal;
  outline-offset: 2px;
}

/* Remove outline for mouse clicks */
:focus:not(:focus-visible) {
  outline: none;
}
```

### Dark Mode Considerations

**Light Mode Support:**
- All components must work in light mode
- Maintain same contrast ratios
- Invert color meanings consistently
- Test both modes thoroughly

**Reduced Motion:**
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Page Templates

### Homepage Hero

**Layout:**
```
Hero Container (Full width, 80vh min)
├─ Content (XL Container, centered)
│  ├─ Eyebrow text ("SEC Filing Workflows")
│  ├─ H1 Headline (2 lines max)
│  ├─ Subheadline (Body Large, 1-2 sentences)
│  ├─ CTA Group (Primary + Secondary button)
│  └─ Trust Indicators (logos, stats, badges)
└─ Hero Visual (Right side, 40% width)
   └─ Abstract illustration or code example
```

**Styling:**
```css
background: Obsidian;
background-image: /* Subtle grid pattern */;
padding: 128px 32px;

h1:
  font-size: 56px;
  font-weight: 700;
  background: linear-gradient(135deg, #F1F5F9, #00D9D9);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 24px;
```

### Service Page

**Layout:**
```
Page Header
├─ Breadcrumb
├─ H1 Title
└─ Description

Service Grid (3 columns, responsive)
├─ Service Card 1
├─ Service Card 2
└─ Service Card 3

Process Section
├─ H2 "How It Works"
└─ Timeline/Steps (vertical on mobile)

Pricing Table (if applicable)

CTA Section
```

### Blog Post

**Layout:**
```
Article Container (Medium Container, 768px)
├─ Article Header
│  ├─ Category badge
│  ├─ H1 Title
│  ├─ Meta (Author, Date, Read time)
│  └─ Featured image
├─ Article Body
│  ├─ Paragraphs (optimal line length)
│  ├─ Headings (H2, H3)
│  ├─ Code blocks
│  ├─ Images
│  └─ Pull quotes
└─ Article Footer
   ├─ Tags
   ├─ Share buttons
   └─ Author bio

Sidebar (optional, desktop only)
├─ Table of contents
└─ Related posts
```

### Case Study Page

**Layout:**
```
Hero Section
├─ Client logo
├─ H1 Title
├─ Key stats (3 metrics)
└─ Hero image

Challenge Section
├─ H2 "The Challenge"
└─ Description + visuals

Solution Section
├─ H2 "Our Solution"
├─ Approach details
└─ Technical implementation

Results Section
├─ H2 "Results"
├─ Metrics (before/after)
└─ Client testimonial

Technical Details (expandable)
├─ Architecture diagram
├─ Code examples
└─ Tools & technologies

CTA Section
```

### Contact Page

**Layout:**
```
Split Layout (50/50)

Left Side:
├─ H1 "Let's Talk"
├─ Subheadline
├─ Contact form
│  ├─ Name field
│  ├─ Email field
│  ├─ Company field
│  ├─ Message textarea
│  └─ Submit button
└─ Privacy note

Right Side:
├─ Contact information
│  ├─ Email
│  ├─ Phone (optional)
│  └─ Office hours
├─ Calendar embed (Calendly)
└─ Social links
```

---

## Implementation Guidelines

### CSS Architecture

**Approach: Utility-First with Tailwind CSS**

**Why Tailwind:**
- Rapid development (bootstrapped agency)
- Consistent design system
- Easy customization
- No CSS bloat
- Community and plugins

**Custom Configuration:**
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        obsidian: '#0A0E1A',
        slate: '#1A1F2E',
        graphite: '#2A2F3E',
        teal: '#00D9D9',
        violet: '#8B5CF6',
        // ... rest of palette
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      // Custom spacing, shadows, etc.
    }
  }
}
```

### Component Library

**Recommended: Radix UI + Custom Styling**

**Why Radix:**
- Unstyled, accessible primitives
- Full keyboard navigation
- ARIA compliant out of the box
- Composable and flexible
- Works perfectly with Tailwind

**Components to Build:**
1. Button variants (Primary, Secondary, Ghost, AI)
2. Input fields and forms
3. Cards (Standard, Feature, Interactive)
4. Navigation (Top nav, Mobile menu)
5. Modal/Dialog
6. Dropdown menus
7. Tooltips
8. Badges and tags
9. Loading states
10. Data tables

### Responsive Design

**Mobile-First Approach:**
```css
/* Base styles (mobile) */
.card {
  padding: 16px;
  margin-bottom: 16px;
}

/* Tablet and up */
@media (min-width: 768px) {
  .card {
    padding: 24px;
    margin-bottom: 24px;
  }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .card {
    padding: 32px;
    margin-bottom: 32px;
  }
}
```

**Testing Viewports:**
- 375px (Mobile - iPhone SE)
- 390px (Mobile - iPhone 12/13)
- 768px (Tablet - iPad)
- 1024px (Laptop - Small)
- 1440px (Desktop - Standard)
- 1920px (Desktop - Large)

### Performance

**Image Optimization:**
- Use WebP format (with fallbacks)
- Lazy load below-the-fold images
- Responsive images (srcset)
- Maximum 200KB per image
- Use SVG for icons and logos

**Font Loading:**
```css
/* Prevent invisible text */
@font-face {
  font-family: 'Inter';
  font-display: swap;
  src: url('/fonts/inter.woff2') format('woff2');
}
```

**Code Splitting:**
- Critical CSS inline
- Defer non-critical JavaScript
- Lazy load components
- Tree shake unused code

**Performance Targets:**
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Time to Interactive: < 3.5s
- Cumulative Layout Shift: < 0.1
- Lighthouse Score: 90+ (all categories)

---

## Brand Applications

### Logo Usage

**Primary Logo:**
- Wordmark + icon
- Horizontal orientation
- Teal icon, white text (dark backgrounds)
- Charcoal text (light backgrounds)

**Icon Only:**
- Use at small sizes (< 100px)
- Minimum size: 24px
- Maintain aspect ratio
- Clear space: 25% of logo height

**Clear Space:**
- Minimum clear space around logo: Height of "o" in wordmark
- No other elements in clear space
- Background should not interfere with legibility

### Marketing Materials

**Business Cards:**
```
Front:
- Logo (top left)
- Name & Title
- Contact info (email, LinkedIn)
- Minimal design, lots of white space

Back:
- Tagline: "Intelligent SEC Filing Workflows"
- Website URL
- Subtle pattern background
```

**Presentation Slides:**
```
Cover Slide:
- Dark background (Obsidian)
- Large title (white)
- Subtitle (Teal)
- Logo (bottom right)

Content Slides:
- Dark or light background
- Large headings (H2)
- Minimal text (bullet points)
- High-quality visuals
- Slide numbers (bottom right)
```

**Email Signature:**
```html
[Name]
Founder, SecFlow Design
✉ email@secflowdesign.com
🌐 secflowdesign.com
🔗 LinkedIn

Intelligent SEC Filing Workflows | Powered by edgartools
```

### Social Media

**Profile Images:**
- Icon only (circular crop)
- Teal on dark background
- Minimum 400x400px

**Cover Images:**
- 1500x500px (LinkedIn)
- 1200x675px (Twitter)
- Branded design with tagline
- Dark background, subtle pattern
- High-quality, professional

**Post Templates:**
```
Square (1080x1080):
- Dark background
- Clear headline (large)
- Supporting visual
- Logo (bottom corner)

Horizontal (1200x630):
- Split layout
- Text left, visual right
- Or full-width background image with overlay text
```

---

## Design Checklist

### Before Launch

**Visual Design:**
- [ ] All colors from approved palette
- [ ] Typography scale consistent throughout
- [ ] Spacing uses 8px grid
- [ ] Shadows and borders consistent
- [ ] Dark mode fully supported
- [ ] Light mode fully supported (if applicable)
- [ ] All images optimized (WebP)
- [ ] Icons consistent size and style
- [ ] Logo usage correct in all contexts

**Interaction:**
- [ ] All buttons have hover states
- [ ] All links underline or change color on hover
- [ ] Loading states for async operations
- [ ] Error states for forms
- [ ] Success confirmations
- [ ] Smooth transitions (200-300ms)
- [ ] No janky animations
- [ ] Cursor changes for interactive elements

**Responsive:**
- [ ] Tested on mobile (375px min)
- [ ] Tested on tablet (768px)
- [ ] Tested on desktop (1440px)
- [ ] Images responsive (srcset)
- [ ] Text readable at all sizes
- [ ] Touch targets 44x44px minimum
- [ ] No horizontal scrolling
- [ ] Navigation works on mobile

**Accessibility:**
- [ ] Color contrast WCAG AA minimum
- [ ] All images have alt text
- [ ] Forms have labels
- [ ] Focus states visible
- [ ] Keyboard navigation works
- [ ] Screen reader tested
- [ ] Semantic HTML used
- [ ] ARIA labels where needed
- [ ] Reduced motion respected

**Performance:**
- [ ] Page load < 3 seconds
- [ ] Images lazy loaded
- [ ] Fonts optimized (font-display: swap)
- [ ] Critical CSS inline
- [ ] JavaScript deferred
- [ ] Lighthouse score 90+
- [ ] No layout shifts
- [ ] Mobile performance tested

**Content:**
- [ ] All placeholder text replaced
- [ ] Headings follow hierarchy
- [ ] Links have clear destinations
- [ ] CTAs clear and compelling
- [ ] Grammar and spelling checked
- [ ] Technical accuracy verified
- [ ] Legal pages included (Privacy, Terms)
- [ ] Contact information correct

**Technical:**
- [ ] Meta tags (title, description)
- [ ] Open Graph tags (social sharing)
- [ ] Favicon (multiple sizes)
- [ ] Apple touch icon
- [ ] Robots.txt
- [ ] Sitemap.xml
- [ ] Analytics configured
- [ ] Forms connected to backend
- [ ] Error pages (404, 500)
- [ ] HTTPS enabled

---

## Conclusion

This design system creates a sophisticated, modern aesthetic that positions SecFlow Design as a premium, technically credible agency operating at the intersection of AI and financial services. The "post-SaaS" design language—characterized by dark interfaces, subtle gradients, intelligent use of teal and violet, and refined typography—differentiates the brand while maintaining the professionalism expected in financial services.

### Key Differentiators

1. **Dark-First Design** - Sophisticated, modern, technical
2. **Teal + Violet Palette** - Unique, intelligent, memorable
3. **Technical Precision** - Every detail considered, nothing arbitrary
4. **AI-Native Visual Language** - Suggests intelligence without cliché
5. **Post-SaaS Aesthetic** - Beyond generic SaaS, refined and purposeful

### Implementation Priority (Bootstrapped)

**Phase 1 (Week 1):**
- Basic color system and typography
- Core components (buttons, inputs, cards)
- Homepage hero section
- Responsive navigation

**Phase 2 (Week 2-3):**
- All page templates
- Full component library
- Dark mode implementation
- Accessibility baseline

**Phase 3 (Month 2-3):**
- Advanced interactions and animations
- Refined micro-interactions
- Performance optimization
- A/B testing visual variants

The design system balances sophistication with practicality, enabling rapid development while maintaining a premium brand presence that resonates with high-value clients in the financial services sector.
