# Technical Writing Style Guide

## Voice & Tone

### The Right Voice for Technical Content

Technical writing should be **professional yet approachable, authoritative yet humble, precise yet engaging**.

#### Active vs. Passive Voice

**Prefer active voice** - it's clearer and more direct.

✓ **Good (Active):**
- "The function returns an object"
- "We initialize the database connection"
- "You can configure the timeout using the flag"
- "This approach reduces memory usage"

✗ **Avoid (Passive):**
- "An object is returned by the function"
- "The database connection is initialized"
- "The timeout can be configured using the flag"
- "Memory usage is reduced by this approach"

**Exception:** Passive voice is acceptable when the actor is unknown or irrelevant:
- "The server was compromised" (unknown attacker)
- "The protocol was designed in 1974" (historical fact)

#### Person & Perspective

**Use second person (you) when giving instructions:**
```markdown
✓ You can install the package with npm install
✗ One can install the package with npm install
✗ The user can install the package with npm install
```

**Use first person plural (we) for shared exploration:**
```markdown
✓ Let's examine why this happens
✓ We'll build a solution step by step
```

**Use first person singular (I) for personal opinions and experiences:**
```markdown
✓ In my experience, this approach works best when...
✓ I've found that async/await improves readability
```

**Avoid third person** unless discussing specific entities:
```markdown
✗ The developer should configure their environment
✓ You should configure your environment
```

### Tone Guidelines

#### Be Conversational
Write as if explaining to a colleague over coffee.

**Conversational:**
> "Here's the thing about closures: they're not as scary as they sound. Basically, a closure is just a function that remembers where it came from."

**Too Formal:**
> "A closure is a mechanism by which a function maintains references to variables in its lexical scope chain."

**Too Casual:**
> "Closures are super cool! They're like functions with memory lol."

#### Be Confident but Humble

**Confident:**
> "This approach solves the problem by eliminating race conditions."

**Arrogant:**
> "This is obviously the only correct solution."

**Too Tentative:**
> "This might possibly maybe help with the issue if you're lucky."

**Balanced:**
> "This approach effectively solves the race condition problem. While other solutions exist, this one balances simplicity with performance."

#### Be Precise but Not Pedantic

**Precise:**
> "This function runs in O(n) time complexity, where n is the array length."

**Pedantic:**
> "Technically, when we say O(n), we're discussing asymptotic upper bounds of the time complexity function as n approaches infinity, disregarding constant factors and lower-order terms."

**Too Vague:**
> "This function is pretty fast."

## Grammar & Mechanics

### Punctuation

#### Commas
**Use the Oxford comma** for clarity:
```
✓ Python, JavaScript, and Go
✗ Python, JavaScript and Go
```

**Use commas to separate clauses:**
```
✓ After initializing the connection, execute the query.
✓ The function runs quickly, but it uses more memory.
```

#### Semicolons
**Avoid semicolons** in technical writing; they make sentences too complex. Use periods instead.

```
✗ The cache improves performance; however, it requires more memory.
✓ The cache improves performance. However, it requires more memory.
```

#### Hyphens & Dashes

**Hyphens (-)** for compound adjectives:
- command-line interface
- server-side rendering
- real-time updates

**En dashes (–)** for ranges:
- pages 10–15
- 2020–2024
- versions 2.0–3.5

**Em dashes (—)** for breaks in thought:
- The solution—despite its complexity—works reliably

#### Quotation Marks

**Use for:**
- Direct quotes: Martin Fowler said, "Any fool can write code that a computer can understand."
- Introducing new terms: This is called "memoization"

**Don't use for:**
- Emphasis (use *italics* or **bold** instead)
- Scare quotes (just state your point clearly)

### Capitalization

#### Headings
**Use sentence case** for most headings:
```
✓ Installing the required dependencies
✗ Installing The Required Dependencies
✗ INSTALLING THE REQUIRED DEPENDENCIES
```

**Title case** for article titles if preferred:
```
✓ A Complete Guide to React Hooks
✓ A complete guide to React hooks
```

Be consistent within your publication.

#### Code & Technical Terms

**Follow official capitalization:**
- JavaScript (not Javascript or javascript)
- TypeScript (not Typescript)
- macOS (not MacOS or Mac OS)
- Node.js (not NodeJS or node.js)
- PostgreSQL (not Postgres, though Postgres is acceptable in casual usage)
- MongoDB (not Mongodb)

**Commands and code remain lowercase:**
```
✓ Run npm install to install dependencies
✗ Run NPM INSTALL to install dependencies
```

### Numbers

**Spell out** numbers one through nine:
- three servers
- five functions
- nine databases

**Use numerals** for 10 and above:
- 15 requests
- 100 milliseconds

**Always use numerals** for:
- Technical specifications: 8 GB RAM, 2.4 GHz
- Version numbers: version 3.2.1
- Measurements: 5 seconds, 10 MB
- Code: port 3000, array[5]
- Percentages: 25% faster

**Exceptions:**
- Start of sentence: "Ten servers were deployed" (or rephrase)
- Informal expressions: "a million times easier"

### Acronyms & Abbreviations

**First use:** Spell out with acronym in parentheses
```
✓ Application Programming Interface (API)
✓ Continuous Integration/Continuous Deployment (CI/CD)
```

**Subsequent uses:** Use the acronym alone
```
✓ The API returns JSON data
✗ The Application Programming Interface returns JSON data
```

**Common acronyms** don't need spelling out:
- HTML, CSS, JavaScript
- HTTP, HTTPS, URL
- API, SDK, CLI
- RAM, CPU, GPU

**Uncommon acronyms** should be defined:
- First use: "We use Content Delivery Networks (CDNs) to..."
- After: "The CDN caches static assets"

## Word Choice

### Simple vs. Complex

**Prefer simple words** when they convey the same meaning:

| Instead of | Use |
|------------|-----|
| utilize | use |
| implement | create, build, add |
| instantiate | create |
| leverage | use |
| facilitate | enable, help |
| terminate | end, stop |
| commence | start, begin |
| subsequently | then, next, later |
| prior to | before |
| in order to | to |

**Exception:** Use technical terms when they're more precise:
- "Instantiate a class" is better than "create a class" in OOP contexts
- "Serialize the data" is better than "convert the data to a string"

### Concrete vs. Abstract

**Be concrete** - use specific examples over abstract concepts:

**Abstract:**
> "This optimization technique can significantly improve application performance metrics."

**Concrete:**
> "This optimization reduces page load time from 3 seconds to 800 milliseconds."

### Inclusive Language

**Use gender-neutral terms:**

| Instead of | Use |
|------------|-----|
| he/she | they |
| his/her | their |
| guys | everyone, folks, team |
| manpower | workforce, staff |
| man-hours | person-hours, work-hours |

**Avoid ableist language:**

| Instead of | Use |
|------------|-----|
| dummy value | placeholder value |
| sanity check | quick check, confidence check |
| crippled | broken, disabled |

**Avoid violent metaphors** when alternatives exist:

| Instead of | Use |
|------------|-----|
| kill the process | stop the process, terminate |
| nuke the database | delete, wipe |
| hit the API | call the API, request |

Note: Some terms like "kill" are so standard in computing that alternatives sound awkward. Use judgment.

### Technical Jargon

**Define before using:**
```markdown
✓ This uses memoization—caching function results to avoid recalculation.
✗ This uses memoization to improve performance.
```

**Provide context for ambiguous terms:**
```markdown
✓ The Git branch (not the code branch) contains...
✓ We'll fork the repository (create a copy), not fork the process (spawn a child process)
```

## Code in Prose

### Inline Code

**Use `backticks` for:**
- Function names: `useState()`
- Variable names: `userEmail`
- File names: `config.json`
- Commands: `npm install`
- Class names: `UserController`
- Package names: `react-router-dom`
- Path names: `/api/users`
- Small code snippets: `const x = 5`

**Examples in sentences:**
```markdown
✓ The `map()` function transforms each element
✓ Store the result in `outputData`
✓ Run `npm start` to launch the server
✓ Import the `useState` hook from React
```

### Code Blocks

**Always specify the language:**
````markdown
```python
def hello():
    print("Hello, World!")
```
````

**Include comments for clarity:**
```javascript
// Initialize the connection pool
const pool = new Pool({
  max: 20,              // Maximum number of clients
  idleTimeoutMillis: 30000  // Close idle clients after 30s
});
```

**Show complete, runnable examples:**
```python
# ✓ Good: Complete example

import requests

def fetch_user(user_id):
    """Fetch user data from API."""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()

# Usage
user = fetch_user(123)
print(user['name'])
```

```python
# ✗ Bad: Incomplete snippet

def fetch_user(user_id):
    response = requests.get(...)
    # ... rest of code
```

**Use comments to explain, not describe:**
```javascript
// ✓ Good: Explains why
// Use exponential backoff to avoid overwhelming the server
const delay = Math.pow(2, retryCount) * 1000;

// ✗ Bad: Describes what (already obvious from code)
// Set delay to 2 to the power of retryCount times 1000
const delay = Math.pow(2, retryCount) * 1000;
```

### Command-Line Examples

**Show the prompt for clarity:**
```bash
$ npm install express
$ node server.js
```

**Or use shell highlighting:**
```shell
npm install express
npm start
```

**Show expected output:**
```bash
$ npm test

> example@1.0.0 test
> jest

 PASS  tests/user.test.js
  ✓ creates user (23 ms)
  ✓ updates user (18 ms)

Tests: 2 passed, 2 total
```

**Indicate multiline commands:**
```bash
docker run \
  --name myapp \
  -p 3000:3000 \
  -v $(pwd):/app \
  myapp:latest
```

## Formatting

### Headings

**Use hierarchy correctly:**
```markdown
# Article Title (H1 - only one per article)

## Major Section (H2)

### Subsection (H3)

#### Minor Point (H4)
```

**Make headings descriptive:**
```markdown
✓ Installing Node.js on Linux
✓ Common Authentication Errors
✗ Installation
✗ Problems
```

**Keep headings parallel:**
```markdown
✓ Setting up the database
✓ Configuring the server
✓ Deploying the application

✗ Setting up the database
✗ Server configuration
✗ How to deploy
```

### Lists

**Use numbered lists** for sequences:
```markdown
1. Install the dependencies
2. Configure the environment
3. Run the migrations
4. Start the server
```

**Use bulleted lists** for unordered items:
```markdown
Features:
- Fast performance
- Low memory usage
- Cross-platform support
```

**Keep list items parallel:**
```markdown
✓ Create the database
✓ Configure the connection
✓ Test the setup

✗ Create the database
✗ Configuring the connection
✗ You should test the setup
```

**Punctuate consistently:**
- If list items are complete sentences, use periods
- If list items are fragments, no periods needed
- Be consistent within each list

### Emphasis

**Bold** for important terms and UI elements:
- Click the **Save** button
- The **API key** is required
- This is **critical** for security

**Italic** for introducing new terms and light emphasis:
- This is called *eventual consistency*
- The process is *similar* to caching
- React uses a *virtual* DOM

**AVOID ALL CAPS** for emphasis - use bold instead:
```markdown
✗ This is VERY IMPORTANT
✓ This is **very important**
```

### Links

**Use descriptive link text:**
```markdown
✓ Read the [React documentation](https://react.dev)
✓ See the [installation guide](https://example.com/install)

✗ Click [here](https://react.dev)
✗ [Link](https://example.com/install)
```

**Provide context for external links:**
```markdown
✓ For more details, see the [Express.js documentation](https://expressjs.com)
✓ The [MDN web docs](https://developer.mozilla.org) explain this in depth
```

### Tables

**Use for comparisons and reference:**
```markdown
| Feature | Option A | Option B |
|---------|----------|----------|
| Speed | Fast | Moderate |
| Memory | High | Low |
| Complexity | Low | High |
```

**Keep cells concise:**
- Use short phrases, not paragraphs
- Break complex tables into multiple simpler ones
- Consider a comparison list if data doesn't fit well in table format

### Callouts & Admonitions

**Use consistent formatting for notes:**

**Information:**
> ℹ️ **Note:** The API requires authentication for all requests.

**Warning:**
> ⚠️ **Warning:** This operation deletes all data and cannot be undone.

**Tip:**
> 💡 **Tip:** You can speed this up by enabling caching.

**Important:**
> ❗ **Important:** Update to version 2.0 before following this guide.

## Common Grammar Mistakes

### Its vs. It's
- **Its** = possessive (The app lost its connection)
- **It's** = it is (It's working correctly)

### Their vs. They're vs. There
- **Their** = possessive (Their code is clean)
- **They're** = they are (They're using React)
- **There** = location or existence (There are three bugs)

### Affect vs. Effect
- **Affect** = verb (This affects performance)
- **Effect** = noun (The effect on performance)
- **Effect** = verb "to cause" (Effect a change - rare in technical writing)

### That vs. Which
- **That** = restrictive (essential to meaning, no comma)
  - "The function that returns null should be fixed"
- **Which** = non-restrictive (additional info, with comma)
  - "The function, which we wrote yesterday, returns null"

### Less vs. Fewer
- **Fewer** = countable (fewer bugs, fewer requests)
- **Less** = uncountable (less memory, less time)

### Ensure vs. Insure vs. Assure
- **Ensure** = make certain (Ensure the connection is secure)
- **Insure** = insurance (rarely used in technical writing)
- **Assure** = reassure someone (I assure you it works)

## Accessibility Guidelines

### Alt Text for Images
```markdown
✓ ![Architecture diagram showing microservices communication](diagram.png)
✗ ![diagram](diagram.png)
✗ ![](diagram.png)
```

### Descriptive Links
Already covered above - never use "click here"

### Color Independence
Don't rely solely on color to convey information:
```markdown
✗ The red items are errors, green items are successful

✓ Errors are marked with ❌ and shown in red.
   Successful items are marked with ✓ and shown in green.
```

### Heading Hierarchy
Always use logical heading order (H1 → H2 → H3), never skip levels

### Meaningful Text
Avoid directional language that assumes visual ability:
```markdown
✗ As you can see in the image above
✓ The following diagram illustrates
✓ The diagram shows three components
```

## Style Checklist

Before publishing, verify:

**Voice & Tone:**
- [ ] Active voice used predominantly
- [ ] Second person ("you") for instructions
- [ ] Conversational but professional tone
- [ ] Confident but not arrogant

**Grammar:**
- [ ] Oxford commas used
- [ ] Numbers formatted consistently
- [ ] Acronyms defined on first use
- [ ] Common grammar mistakes avoided

**Code:**
- [ ] All code examples tested
- [ ] Language specified for syntax highlighting
- [ ] Inline code uses backticks
- [ ] Examples are complete and runnable

**Formatting:**
- [ ] Heading hierarchy is logical
- [ ] Lists are parallel in structure
- [ ] Links use descriptive text
- [ ] Emphasis used appropriately

**Accessibility:**
- [ ] Images have alt text
- [ ] Links are descriptive
- [ ] Color not sole indicator
- [ ] Heading order is correct

**Consistency:**
- [ ] Technical terms capitalized correctly
- [ ] One style throughout (not mixed)
- [ ] Terminology used consistently

---

*Consistent style makes your writing more professional and easier to read. When in doubt, prioritize clarity over cleverness.*
