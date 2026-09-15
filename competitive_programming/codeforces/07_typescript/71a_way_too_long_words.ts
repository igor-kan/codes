function wayTooLong(word: string): string {
  return word.length <= 10 ? word : `${word[0]}${word.length - 2}${word[word.length - 1]}`;
}

if (wayTooLong("word") !== "word") throw new Error("way too long failed");
if (wayTooLong("localization") !== "l10n") throw new Error("way too long failed");
if (wayTooLong("internationalization") !== "i18n") throw new Error("way too long failed");
console.log("71A way too long words ok");
