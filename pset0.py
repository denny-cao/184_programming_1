import numpy as np
import matplotlib.pyplot as plt
import sys # Use for cmd line args

A = np.array([[0,2,4],[2,4,2],[3,3,1]])
b = np.array([-2,-2,-4])
c = np.array([1,1,1])

def q1_a():
    """
    Return A^{-1}
    """
    return np.linalg.inv(A)

def q1_b():
    """
    Return A^{-1}b, Ac
    """
    return np.linalg.inv(A).dot(b), A.dot(c)

def q2_a(n):
    Z = np.random.randn(n)
    plt.step(sorted(Z), np.arange(1,n+1)/float(n))

def q2_b(n):
    for k in [1, 8, 64, 512]:
        Yk = 1.0/np.sqrt(k) * np.sum(np.sign(np.random.randn(n,k)), axis=1)
        plt.step(sorted(Yk), np.arange(1,n+1)/float(n))

def create_graph(n):
    q2_a(n)
    q2_b(n)
    plt.legend(["Gaussian", "1", "8", "64", "512"])
    plt.xlabel("Observations")
    plt.ylabel("Probability")
    plt.ylim(0,1)
    plt.xlim(-3,3)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pset0.py <question>")
        sys.exit(1)
    question = sys.argv[1]
    if question == "1a":
        print(q1_a())
    elif question == "1b":
        print(q1_b())
    elif question == "2a":
        q2_a(40000)
        plt.show()
    elif question == "2b":
        q2_b(40000)
        plt.show()
    elif question == "2":
        create_graph(40000)
    else:
        print("Invalid question")
        sys.exit(1)


