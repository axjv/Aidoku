import Testing
import UIKit
import AsyncDisplayKit

@testable import Aidoku

@MainActor
struct GIFImageNodeTests {
    @Test func resetClearsStoredImageBeforeViewMaterializes() {
        let node = GIFImageNode()
        node.image = UIImage()
        #expect(node.image != nil)

        node.reset()

        #expect(node.image == nil)
        #expect(node.animatedData == nil)
    }

    @Test func resetClearsMaterializedImageView() async {
        let node = GIFImageNode()
        _ = node.view
        node.image = UIImage()
        await Task.yield()
        #expect(node.imageView?.image != nil)

        node.reset()
        await Task.yield()

        #expect(node.image == nil)
        #expect(node.animatedData == nil)
        #expect(node.imageView?.image == nil)
    }
}
