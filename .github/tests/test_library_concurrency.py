from pathlib import Path

manager = Path("Aidoku/Core/Library/Services/MangaManager.swift").read_text()
settings = Path("Aidoku/Core/Settings/Library/LibrarySettings.swift").read_text()
ui = Path("Aidoku/Features/Settings/Settings.swift").read_text()

assert "withTaskGroup(" in manager
assert "let requestedConcurrency = Int(AppSettings.library.concurrentUpdates.get()) ?? 3" in manager
assert "max(1, min(requestedConcurrency, Self.maxConcurrentLibraryUpdateTasks))" in manager
assert "let initialCount = min(concurrentUpdates, refreshItems.count)" in manager
assert "if nextIndex < refreshItems.count" in manager
assert "private static let maxConcurrentLibraryUpdateTasks = 10" in manager
assert 'SettingsKey<String>("Library.concurrentUpdates", default: "3")' in settings
for value in ["1", "2", "3", "4", "6", "8", "10"]:
    assert f'"{value}"' in ui
assert "lastRefreshAttempt" not in manager
print("library concurrency regression checks passed")
