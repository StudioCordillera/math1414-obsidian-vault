# 🧪 ANKI FLASHCARD CONNECTION TEST

## Step 1: Install AnkiConnect Add-on

**In Anki (currently running):**
1. **Tools → Add-ons → Get Add-ons**
2. **Enter code:** `2055492159`
3. **Click OK** to install AnkiConnect

## Step 2: Configure AnkiConnect

1. **Tools → Add-ons → AnkiConnect → Config**
2. **Replace ALL text** with this exact configuration:

```json
{
  "apiKey": null,
  "apiLogPath": null,
  "webBindAddress": "127.0.0.1",
  "webBindPort": 8765,
  "webCorsOrigin": "http://localhost",
  "webCorsOriginList": ["http://localhost", "app://obsidian.md"]
}
```

3. **Click OK** and **restart Anki**

## Step 3: Test Math Flashcard Creation

Once AnkiConnect is working, I'll create a test flashcard with this sample math problem:

**Front:** Find (f ∘ g)(x) if f(x) = 2x + 1 and g(x) = x² - 3
**Back:** (f ∘ g)(x) = f(g(x)) = f(x² - 3) = 2(x² - 3) + 1 = 2x² - 6 + 1 = 2x² - 5

## Step 4: Install Obsidian Note Synchronizer

**In Obsidian:**
1. **Settings → Community Plugins**
2. **Search:** "Note Synchronizer"
3. **Install and Enable**

## ✅ Success Indicators

When working, you should see:
- ✅ AnkiConnect API responding
- ✅ Test flashcard created in Anki
- ✅ Obsidian can sync notes to Anki
- ✅ Math problems become spaced repetition cards

---

## 🎯 Current Status: Waiting for AnkiConnect Installation

**Next Action:** Install AnkiConnect add-on in Anki, then run connection test.