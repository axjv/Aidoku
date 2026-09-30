from pathlib import Path

path = Path("Aidoku/Core/Database/CoreDataManager+Chapter.swift")
text = path.read_text()
start = text.index("    func setChapters(")
end = text.index("\n    /// Get the number of unread chapters", start)
body = text[start:end]

assert "incomingChapters: [String: (offset: Int, chapter: AidokuRunner.Chapter)]" in body
assert "incomingChapters[chapter.id] == nil" in body
assert "incomingChapters.removeValue(forKey: object.id)" in body
assert "for (offset, chapter) in chapters.enumerated()" in body
assert "guard incomingChapters.removeValue(forKey: chapter.id) != nil else { continue }" in body
assert ".first(where:" not in body
assert ".removeAll" not in body
assert "hasChapter(" not in body
print("chapter reconciliation regression checks passed")
