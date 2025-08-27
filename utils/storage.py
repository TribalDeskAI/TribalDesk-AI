import streamlit as st
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def save_email(email: str, interest: str = ""):
    ensure_data_dir()
    f = DATA_DIR / "emails.csv"
    if f.exists():
        df = pd.read_csv(f)
    else:
        df = pd.DataFrame(columns=["email","interest"])
    if email not in df["email"].values:
        df.loc[len(df)] = [email, interest]
        df.to_csv(f, index=False)

def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def save_csv(path: Path, df: pd.DataFrame):
    df.to_csv(path, index=False)
