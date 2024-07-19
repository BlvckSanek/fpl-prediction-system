from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    team = Column(String)
    position = Column(String)
    total_points = Column(Integer)
    current_price = Column(Float)
    start_season_price = Column(Float)
    goals_scored = Column(Integer)
    assists = Column(Integer)
    clean_sheets = Column(Integer)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    minutes_played = Column(Integer)
    selected_by_percent = Column(Float)
    bonus_points = Column(Integer)
    transfers_in = Column(Integer)
    transfers_out = Column(Integer)
    form = Column(Float)

    performances = relationship("PlayerPerformance", back_populates="player")


class Fixture(Base):
    __tablename__ = "fixtures"

    id = Column(Integer, primary_key=True)
    fixture_id = Column(Integer)
    date = Column(DateTime)
    home_team = Column(String)
    away_team = Column(String)
    home_team_score = Column(Integer)
    away_team_score = Column(Integer)
    venue = Column(String)

    performances = relationship("PlayerPerformance", back_populates="fixture")


class PlayerPerformance(Base):
    __tablename__ = "player_performances"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    fixture_id = Column(Integer, ForeignKey("fixtures.id"))
    points = Column(Integer)
    minutes_played = Column(Integer)
    goals_scored = Column(Integer)
    assists = Column(Integer)
    clean_sheets = Column(Integer)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    bonus_points = Column(Integer)

    player = relationship("Player", back_populates="performances")
    fixture = relationship("Fixture", back_populates="performances")


def init_db():
    """Initialize the database."""
    engine = create_engine("sqlite:///data/fpl.db")
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
