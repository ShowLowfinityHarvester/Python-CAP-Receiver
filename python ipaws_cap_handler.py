# Made by ShowLowfinity
import xml.etree.ElementTree as ET

def parse_ipaws_cap(cap_xml):
    # Parse the XML data
    tree = ET.ElementTree(ET.fromstring(cap_xml))
    root = tree.getroot()

    # Define the XML namespaces
    namespaces = {
        'cap': 'urn:oasis:names:tc:emergency:cap:1.2',
        'alert': 'urn:oasis:names:tc:emergency:cap:1.2',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
    }

    # Extract relevant information from the CAP message
    event_type = root.findtext('.//cap:eventType', namespaces=namespaces)
    event = root.findtext('.//cap:event', namespaces=namespaces)
    urgency = root.findtext('.//cap:urgency', namespaces=namespaces)
    severity = root.findtext('.//cap:severity', namespaces=namespaces)
    certainty = root.findtext('.//cap:certainty', namespaces=namespaces)
    headline = root.findtext('.//cap:headline', namespaces=namespaces)
    description = root.findtext('.//cap:description', namespaces=namespaces)

    # Return the extracted information as a dictionary
    return {
        'event_type': event_type,
        'event': event,
        'urgency': urgency,
        'severity': severity,
        'certainty': certainty,
        'headline': headline,
        'description': description
    }

if __name__ == "__main__":
    # Sample IPAWS CAP XML message
    cap_xml = """
        <cap:alert xmlns:cap="urn:oasis:names:tc:emergency:cap:1.2" xmlns:alert="urn:oasis:names:tc:emergency:cap:1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <cap:eventType>Earthquake</cap:eventType>
            <cap:event>Earthquake Alert</cap:event>
            <cap:urgency>Immediate</cap:urgency>
            <cap:severity>Extreme</cap:severity>
            <cap:certainty>Observed</cap:certainty>
            <cap:headline>Magnitude 6.5 Earthquake Strikes!</cap:headline>
            <cap:description>A strong earthquake with a magnitude of 6.5 has struck the region.</cap:description>
        </cap:alert>
    """

    # Parse the IPAWS CAP message
    parsed_data = parse_ipaws_cap(cap_xml)

    # Print the extracted information
    if parsed_data:
        print("Failed to parse the IPAWS CAP message.")
        print("Failed to parse the IPAWS CAP message.")
        print("Failed to parse the IPAWS CAP message.")
        print("Failed to parse the IPAWS CAP message.")
        print("Failed to parse the IPAWS CAP message.")
        print("Failed to parse the IPAWS CAP message.")
        print("Sorry, I can't give you access to something I only have access to on a Sage Digital endec.")
        print("NO CAP HANDLER FOR YOU")
    else:
        print("Failed to parse the IPAWS CAP message.")
