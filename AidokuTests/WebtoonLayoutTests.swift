import Testing
import UIKit

@testable import Aidoku

@MainActor
struct WebtoonLayoutTests {
    @Test func readerSliderKeepsValueGeometryAfterResize() throws {
        let slider = ReaderSliderView(frame: CGRect(x: 0, y: 0, width: 1500, height: 12))
        slider.currentValue = 5.0 / 11.0
        slider.setNeedsLayout()
        slider.layoutIfNeeded()

        slider.frame = CGRect(x: 0, y: 0, width: 678, height: 12)
        slider.setNeedsLayout()
        slider.layoutIfNeeded()

        let thumb = try #require(slider.subviews.first(where: { abs($0.bounds.height - 30) < 0.5 }))
        let expectedPosition = 5 + (slider.bounds.width - 10) * slider.currentValue

        #expect(abs(thumb.frame.midX - expectedPosition) < 1)
        #expect(thumb.frame.midX < slider.bounds.midX)
    }
}
