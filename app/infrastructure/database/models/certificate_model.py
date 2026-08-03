from sqlalchemy import Column, String, Date, ForeignKey

from app.infrastructure.database.base import Base


class CertificateModel(Base):
    __tablename__ = "certificates"

    id = Column(String, primary_key=True)
    professional_id = Column(
        String,
        ForeignKey("professionals.id"),
        nullable=False,
    )

    name = Column(String, nullable=False)
    issuer = Column(String, nullable=False)
    credential_id = Column(String, nullable=False)
    issued_date = Column(Date, nullable=False)
    expiry_date = Column(Date)
    verification_url = Column(String)
    status = Column(String, nullable=False)