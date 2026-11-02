# L’ATELIER · iOS APP STORE & TESTFLIGHT DEPLOYMENT GUIDE

This document details the exact process for running **L’Atelier** as an authentic native iOS app using Apple Xcode, deploying to physical iPhones via TestFlight, and submitting to the Apple App Store.

---

## 1. Instant iOS PWA Testing (No Mac Required)

L'Atelier is fully configured as a Progressive Web App (PWA) with native iOS safe-area handling:

1. Open the deployed URL in **Mobile Safari** on your iPhone or iPad.
2. Tap the **Share** button (the square with an arrow pointing upward).
3. Scroll down and tap **Add to Home Screen**.
4. Tap **Add** in the top-right corner.
5. Tap the **L’Atelier** gold monogram icon on your home screen.

> **Result:** L'Atelier launches in full-screen standalone mode with no Safari address bar or navigation buttons. It respects the Dynamic Island and notch, keeps cooking timers running, and functions fully offline.

---

## 2. Compiling the Native iOS App with Xcode & Capacitor

L'Atelier includes a configured `capacitor.config.json` that packages the exact zero-build HTML5, CSS, and ES6+ engine into an authentic Apple Xcode project using `WKWebView`.

### Prerequisites
- macOS computer running macOS Sonoma or Sequoia.
- **Xcode** (free download from Mac App Store) with iOS SDK and Command Line Tools installed.
- **Node.js** (v18 or higher) and npm.
- An **Apple Developer Account** (for App Store and TestFlight distribution).

### Step-by-Step Build Commands

Open Terminal in the `latelier` project directory:

```bash
# 1. Install Capacitor dependencies
npm install

# 2. Add the native iOS platform (creates the native /ios Xcode workspace)
npx cap add ios

# 3. Synchronize all web assets (HTML, JS datasets, CSS, icons) into the native bundle
npx cap sync ios

# 4. Open the generated project in Xcode
npx cap open ios
```

---

## 3. Configuring Xcode for App Store & TestFlight

Once Xcode opens `App.xcworkspace`:

1. **Select the Project Target:**
   - In the left sidebar, click the top **App** project item.
   - Under **Targets**, click **App**.

2. **Set Signing & Team:**
   - Click the **Signing & Capabilities** tab.
   - Check **Automatically manage signing**.
   - Under **Team**, select your Apple Developer Team.
   - Verify the Bundle Identifier: `com.latelier.culinary`.

3. **Set Display Name & Orientations:**
   - In the **General** tab:
     - **Display Name:** `L'Atelier`
     - **Deployment Target:** iOS 15.0 or higher.
     - **Supported Orientations:** Portrait, Landscape Left, Landscape Right.

4. **Test on Simulator or Physical iPhone:**
   - Connect your iPhone via USB / Wi-Fi, select it in the top device menu, and press **Cmd + R** (Run).

---

## 4. Submitting to TestFlight & The App Store

1. In Xcode, select **Product ➔ Destination ➔ Any iOS Device (arm64)**.
2. Click **Product ➔ Archive**.
3. When the Organizer window opens:
   - Click **Distribute App**.
   - Select **App Store Connect**.
   - Select **Upload** to send the build directly to TestFlight.
4. Log into [App Store Connect](https://appstoreconnect.apple.com/):
   - Under **TestFlight**, invite external or internal culinary testers.
   - Under **App Store**, provide screenshots, description, keywords, and submit for Apple Review!
