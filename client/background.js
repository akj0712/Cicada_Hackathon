const defaultFilters = [
  "*://*.doubleclick.net/*",
  "*://partner.googleadservices.com/*",
  "*://*.googlesyndication.com/*",
  "*://*.google-analytics.com/*",
  "*://creative.ak.fbcdn.net/*",
  "*://*.adbrite.com/*",
  "*://*.exponential.com/*",
  "*://*.quantserve.com/*",
  "*://*.scorecardresearch.com/*",
  "*://*.zedo.com/*",
];

chrome.webRequest.onBeforeRequest.addListener(
  function (details) {
    return { cancel: true };
  },
  { urls: defaultFilters },
  ["blocking"]
);

chrome.tabs.getSelected(null, function (tab) {
  tabUrl = tab.url;
  alert(tabUrl);
});

// chrome.windows.runtime.getAll({ populate: true }, function (windows) {
//   windows.forEach(function (window) {
//     window.tabs.forEach(function (tab) {
//       console.log(tab.url);
//     });
//   });
// });
