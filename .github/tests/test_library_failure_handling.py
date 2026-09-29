from pathlib import Path

manager = Path("Aidoku/Core/Library/Services/MangaManager.swift").read_text()
settings = Path("Aidoku/Core/Settings/Library/LibrarySettings.swift").read_text()
localized = Path("Aidoku/App/Resources/Localization/en.lproj/Localizable.strings").read_text()

assert "Task<Bool, Never>" in manager
assert "lastRefreshAttempt" in manager
assert "lastRefreshAttempt" in settings
assert "LibraryRefreshFailure" in manager
assert "try await source.getMangaUpdate" in manager
assert "try? await SourceManager.shared.source" not in manager
assert "context.rollback()" in manager
assert "failures.isEmpty" in manager
assert 'NSLocalizedString("LIBRARY_REFRESH_INCOMPLETE")' in manager
assert "[MangaIdentifier: AidokuRunner.Manga]" in manager
assert "mangaItem.identifier" in manager
assert "(mangaObject.langFilter == nil || chapter.lang == mangaObject.langFilter)" in manager
assert "(scanlatorFilter.isEmpty || scanlatorFilter.contains" in manager
refresh_start = manager.index("    private func doLibraryRefresh(")
refresh_end = manager.index("    private func updateLibraryRefreshProgress", refresh_start)
refresh_body = manager[refresh_start:refresh_end]
assert "withTaskGroup(" not in refresh_body
assert "concurrentUpdates" not in refresh_body
assert '"LIBRARY_REFRESH_INCOMPLETE"' in localized
print("library failure-handling regression checks passed")
