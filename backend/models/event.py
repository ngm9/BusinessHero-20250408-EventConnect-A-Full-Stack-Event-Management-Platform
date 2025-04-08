from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base

# TODO: Define Event model with appropriate fields and relationships
# Consider fields like title, description, date, location, capacity, etc.
# Consider relationships with users (organizers, attendees) and other entities