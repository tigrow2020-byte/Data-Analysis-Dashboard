import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def get_stats():
    df = pd.read_csv("students.csv")
    stats = {
        "total": len(df),
        "average": round(df["marks"].mean(), 2),
        "highest": df["marks"].max(),
        "lowest": df["marks"].min(),
        "top_student": df.loc[df["marks"].idxmax(), "name"]
    }
    return stats

def create_graph():
    df = pd.read_csv("students.csv")
    plt.figure(figsize=(8, 4))
    plt.bar(df["name"], df["marks"], color="blue")
    plt.title("Student Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.savefig("static/graph.png")
    plt.close()
