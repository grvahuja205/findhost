import sys
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class AmiInitial(Base):
	__tablename__ = 'ami'
	server_name_initial = Column(String(100), nullable = False)
	console_initial = Column(String(10), nullable = False, default = 'AMI')
	monitoring_source_initial = Column(String(40), nullable = False)

class MlmFinal(Base):
	__tablename__ = 'mlm_final'
	server_name = Column(String(100), nullable = False)
	console = Column(String(10), nullable = False)
	severity = Column(String(10))
	monitoring_source = Column(String(100), nullable = False)
	account_code = Column(String(10))
	account_name = Column(String(100))

class EkgFinal(Base):
	__tablename__ = 'ekg_final'
	server_name = Column(String(100), nullable = False)
	console = Column(String(10), nullable = False, default = 'EKG')
	severity = Column(String(5), nullable = False)
	monitoring_source = Column(String(100), nullable = False)
	account_code = Column(String(10))
	account_name Column(String(100))

class AmiFinal(Base):
	__tablename__ = 'ami_final'
	server_name = Column(String(100), nullable = False)
	console = Column(String(10), nullable = False, default = 'AMI')
	severity = Column(String(5))
	monitoring_source = Column(String(100), nullable = False)
	account_code = Column(String(10))
	account_name = Column(String(100))

class AmmFinal(Base):
	__tablename__ = 'amm_final'
	server_name = Column(String(100), nullable = False)
	console = Column(String(10), nullable = False, default = 'AMM')
	severity = Column(String(5))
	monitoring_source = Column(String(100), nullable = False)
	account_code = Column(String(10))
	account_name = Column(String(100))

engine = create_engine("mysql://root:root@localhost/findhost")

Base.metadata.drop(AmiInitial, checkfirst=True)
Base.metadata.create(AmiInitial, checkfirst=True)

Base.metadata.drop(AmiFinal, checkfirst=True)
Base.metadata.create(AmiFinal, checkfirst=True)

Base.metadata.drop(MlmFinal, checkfirst=True)
Base.metadata.create(MlmFinal, checkfirst=True)

Base.metadata.drop(EkgFinal, checkfirst=True)
Base.metadata.create(EkgFinal, checkfirst=True)

Base.metadata.drop(AmmFinal, checkfirst=True)
Base.metadata.create(AmmFinal, checkfirst=True)