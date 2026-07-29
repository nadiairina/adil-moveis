use framework "Foundation"
use framework "Vision"
use framework "AppKit"

on run argv
    set imagePath to item 1 of argv
    set theURL to current application's NSURL's fileURLWithPath:imagePath
    set req to current application's VNRecognizeTextRequest's alloc()'s init()
    set handler to current application's VNImageRequestHandler's alloc()'s initWithURL:theURL options:(current application's NSDictionary's alloc()'s init())
    handler's performRequests:{req} |error|:(missing value)
    set results to req's results()
    set outText to ""
    repeat with res in results
        set txt to (res's topCandidates:1)'s firstObject()'s |string|() as text
        set outText to outText & txt & return
    end repeat
    return outText
end run
