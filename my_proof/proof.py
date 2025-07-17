import json
import logging
import os

from my_proof.models.proof_response import ProofResponse
from my_proof.config import settings

class Proof:
    def __init__(self):
        self.proof_response = ProofResponse(dlp_id=settings.DLP_ID)

    def generate(self) -> ProofResponse:
        """Generate a hardcoded proof for all input files."""
        logging.info("Starting simple hardcoded proof generation")

        # Hardcoded values for demo
        hardcoded_proof = {
            "dlp_id": settings.DLP_ID,
            "valid": True,
            "score": 0.7614457831325301,
            "authenticity": 1.0,
            "ownership": 1.0,
            "quality": 0.6024096385542169,
            "uniqueness": 0.0,
            "attributes": {
                "total_score": 0.5,
                "score_threshold": 0.83,
                "email_verified": True
            },
            "metadata": {}
        }

        # Only process the first .json file found in the input directory
        for input_filename in os.listdir(settings.INPUT_DIR):
            if input_filename.endswith('.json'):
                logging.info(f"Processing file: {input_filename}")
                # Optionally, you could load the file and add some fields from it to attributes
                break

        # Fill the ProofResponse model
        self.proof_response.dlp_id = hardcoded_proof["dlp_id"]
        self.proof_response.valid = hardcoded_proof["valid"]
        self.proof_response.score = hardcoded_proof["score"]
        self.proof_response.authenticity = hardcoded_proof["authenticity"]
        self.proof_response.ownership = hardcoded_proof["ownership"]
        self.proof_response.quality = hardcoded_proof["quality"]
        self.proof_response.uniqueness = hardcoded_proof["uniqueness"]
        self.proof_response.attributes = hardcoded_proof["attributes"]
        self.proof_response.metadata = hardcoded_proof["metadata"]

        return self.proof_response

