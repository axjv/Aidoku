from pathlib import Path

text = Path("Aidoku/Core/Sources/BuiltIn/Kavita/KavitaHelper.swift").read_text()
start = text.index("        func doRequest(baseUrl: URL)")
end = text.index("\n        func tryRequests", start)
body = text[start:end]
decoder = body.index("let decoder = JSONDecoder()")
strategy = body.index("decoder.dateDecodingStrategy")
assert body[:decoder].count("DateFormatter()") == 2
assert body[strategy:].count("DateFormatter()") == 0
assert 'Locale(identifier: "en_US_POSIX")' in body
assert '"yyyy-MM-dd\'T\'HH:mm:ss.SSSSSSS"' in body
assert '"yyyy-MM-dd\'T\'HH:mm:ss"' in body
assert "fractionalDateFormatter.date(from: string)" in body
assert "dateFormatter.date(from: string)" in body
print("Kavita formatter regression checks passed")
