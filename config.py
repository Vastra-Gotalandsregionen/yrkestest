import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'välj-något-bättre-än-detta'
