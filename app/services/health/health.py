from app.services.health.models import Health, Check

def health() -> Health:
  """
    Check for the health of the application 
  """
  return Health(
    alive=isAlive()
  )

def isAlive() -> Check:
  return Check(success=True, title="Check if API service is alive")