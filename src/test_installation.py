# Create test_installation.py in the src folder
"""
Test script to verify AI development environment setup.
Run this script to ensure all libraries are working correctly.
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets

def test_numpy():
    """Test NumPy functionality"""
    print("\n ****Testing NumPy...****")
    # Create arrays
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"  Array shape: {arr.shape}")
    print(f"  Array sum: {np.sum(arr)}")
    print(f"  NumPy version: {np.__version__}")
    return True

def test_pandas():
    """Test Pandas functionality"""
    print("\n ****Testing Pandas...****")
    # Create DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 92, 78]
    })
    print(f"  DataFrame shape: {df.shape}")
    print(f"  Column names: {list(df.columns)}")
    print(f"  Mean age: {df['Age'].mean():.1f}")
    print(f"  Pandas version: {pd.__version__}")
    return True

def test_matplotlib():
    """***Test Matplotlib functionality***"""
    print("\n ****Testing Matplotlib...****")
    # Create simple plot
    plt.figure(figsize=(4, 3))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.title("Test Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    
    # Save plot to outputs folder
    import os
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    plt.savefig('outputs/test_plot.png')
    plt.close()
    print(f"  Plot saved to outputs/test_plot.png")
    print(f"  Matplotlib version: {plt.matplotlib.__version__}")
    return True

def test_sklearn():
    """Test scikit-learn functionality"""
    print("\n ****Testing scikit-learn...***")
    # Load dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    print(f"  Iris dataset shape: {X.shape}")
    print(f"  Target classes: {np.unique(y)}")
    print(f"  scikit-learn version: {sklearn.__version__}")
    return True

def main():
    """Main test function"""
    print("=" * 50)
    print(" AI Development Environment Verification")
    print("=" * 50)
    
    # Test Python version
    print(f"\nPython version: {sys.version}")
    
    # Run all tests
    tests = [
        test_numpy(),
        test_pandas(),
        test_matplotlib(),
        test_sklearn()
    ]
    
    # Summary
    print("\n" + "=" * 50)
    if all(tests):
        print("***ALL TESTS PASSED! Environment is ready for AI development.")
    else:
        print(" Some tests failed. Please check installations.")
    print("=" * 50)

if __name__ == "__main__":
    main()

