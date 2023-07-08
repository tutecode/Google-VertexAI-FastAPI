# Design and test your own prompts

import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="ghc-010", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """The Third Test of the 1948 Ashes series was one of five Tests in the Ashes cricket series between Australia and England. It was played at Old Trafford in Manchester from 8 to 13 July 1948. After a bouncer by Ray Lindwall bloodied his head, Denis Compton left the field but returned and helped England recover to 363 all out on the second afternoon. Compton and Alec Bedser were involved in a mix-up, running out the latter and ending a 121-run partnership. Dick Pollard hit Australian Sid Barnes (pictured) in the ribs with a pull shot, hospitalising him. After rain washed out the fourth day and the first half of the fifth day, the match was drawn, meaning that England could do no better than level the series.""",
    **parameters
)
print(f"Response from Model: {response.text}")