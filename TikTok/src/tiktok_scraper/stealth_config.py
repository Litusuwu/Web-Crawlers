"""Stealth configuration for headless browser evasion.

Configures anti-detection measures across multiple signal layers
to minimize TikTok's ability to identify automated browsers.
"""

STEALTH_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--disable-features=IsolateOrigins,site-per-process",
    "--disable-infobars",
    "--disable-dev-shm-usage",
    "--no-first-run",
    "--no-default-browser-check",
    "--disable-background-networking",
    "--disable-breakpad",
    "--disable-component-update",
    "--disable-domain-reliability",
    "--disable-sync",
    "--metrics-recording-only",
    "--no-service-autorun",
]

VIEWPORT = {"width": 1920, "height": 1080}

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)

STEALTH_JS_OVERRIDES = """
// Remove webdriver property from navigator prototype
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined,
});
delete navigator.__proto__.webdriver;

// Ensure chrome object exists with expected properties
if (!window.chrome) {
    window.chrome = {};
}
if (!window.chrome.runtime) {
    window.chrome.runtime = {};
}

// Override permissions query for notifications
const originalQuery = window.navigator.permissions.query;
window.navigator.permissions.query = (parameters) =>
    parameters.name === 'notifications'
        ? Promise.resolve({ state: Notification.permission })
        : originalQuery(parameters);

// Fake plugins array
Object.defineProperty(navigator, 'plugins', {
    get: () => [
        { name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer' },
        { name: 'Chrome PDF Viewer', filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai' },
        { name: 'Native Client', filename: 'internal-nacl-plugin' },
    ],
});

// Fake languages
Object.defineProperty(navigator, 'languages', {
    get: () => ['en-US', 'en'],
});

// Fix toString for overridden functions
const nativeToString = Function.prototype.toString;
const nativeToStringStr = nativeToString.call(nativeToString);
const overrides = new Map();
const replaceWithNative = (obj, prop, replacement) => {
    const original = obj[prop];
    obj[prop] = replacement;
    overrides.set(replacement, nativeToString.call(original));
};
Function.prototype.toString = function () {
    if (overrides.has(this)) return overrides.get(this);
    return nativeToString.call(this);
};
"""
