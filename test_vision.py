try:
    import Vision
    import Quartz
    print("Vision framework available!")
except ImportError as e:
    print("Import error:", e)
