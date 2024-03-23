from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData

def process_agent_data(agent_data: AgentData) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    state = "poor"
    if agent_data.accelerometer.y < -10:
        state = "excellent"
    elif -10 <= agent_data.accelerometer.y < 10:
        state = "average"
        
    return ProcessedAgentData(road_state = state, agent_data = agent_data)