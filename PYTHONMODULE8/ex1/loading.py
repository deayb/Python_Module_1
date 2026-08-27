def check_dependencies() -> dict:
    status = {}

    try:
        import pandas
        status["pandas"] = pandas.__version__
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ModuleNotFoundError:
        status["pandas"] = None
        print("[MISSING] pandas - install with: pip install pandas")

    try:
        import numpy
        status["numpy"] = numpy.__version__
        print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
    except ModuleNotFoundError:
        status["numpy"] = None
        print("[MISSING] numpy - install with: pip install numpy")

    try:
        import matplotlib
        status["matplotlib"] = matplotlib.__version__
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    except ModuleNotFoundError:
        status["matplotlib"] = None
        print("[MISSING] matplotlib - install with: pip install matplotlib")