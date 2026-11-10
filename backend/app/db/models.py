import datetime
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from app.db.database import Base

class SeniorProfile(Base):
    __tablename__ = "senior_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_uid = Column(String(100), unique=True, index=True, nullable=False)
    senior_name = Column(String(150), default="વડીલ (Senior User)")
    preferred_language = Column(String(10), default="gu")
    caregiver_name = Column(String(150), default="દીકરો / દીકરી (Family Caregiver)")
    caregiver_phone = Column(String(25), default="")
    caregiver_relation = Column(String(50), default="દીકરો (Son)")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class ScamReportLog(Base):
    __tablename__ = "scam_report_logs"

    id = Column(Integer, primary_key=True, index=True)
    submitted_text = Column(Text, nullable=True)
    language = Column(String(10), default="gu")
    is_scam = Column(Boolean, default=False)
    risk_score = Column(Integer, default=0)
    verdict_title = Column(String(255), default="")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

