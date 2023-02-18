# Installing and loading necessary packages -----------------------
import torch
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import torch.nn as nn
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import json
