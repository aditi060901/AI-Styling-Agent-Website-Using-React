# AI-Styling-Agent-Website-Using-React

Extracted features files were too big to be uploaded..Below is the link from where the image datasets were downloaded:

https://universe.roboflow.com/search?q=class%3Adress

Image pre-processing and features extraction process is in extract.py file

**Introduction**

Selecting outfits from a wardrobe can often be a time- consuming and overwhelming task, as individuals 
face decision fatigue and struggle to coordinate pieces, creating a growing need for an intelligent styling agent that 
simplifies the process and provides fashion recommendations. The rapid advancements in artificial intelligence and 
deep learning have revolutionized numerous industries, and fashion is no exception. 
Personalized fashion recommendations, tailored to individual preferences and styles, have emerged as a 
significant application area. This research introduces a novel website platform designed to provide users with 
curated outfit suggestions based on their personal wardrobes. The platform leverages the power of convolutional 
neural networks (CNNs), specifically the ResNet50 model, to analyze and understand the visual characteristics of 
clothing items. Users can upload images of their wardrobe items to the platform, where they are organized into 
personalized folders. By combining these items into various outfit combinations, the system extracts deep visual 
features using the ResNet50 model, capturing essential information about the style, color, and overall aesthetic of 
each outfit. 
The key aspect of this approach lies in the comparison of user-generated outfit combinations with a vast 
dataset of pre-stored outfits. To assess similarity and identify the most suitable outfits for the user, the system 
employs Euclidean distance to calculate the proximity between the feature vectors extracted from the user’s 
combinations and those from the dataset. This paper delves into the technical framework underlying the 
implementation of the CNN model, feature extraction processes, and the distance-based recommendation system. It 
explores the efficacy of ResNet50 in capturing meaningful visual features and discusses the role of Euclidean 
distance in producing accurate and relevant outfit suggestions. This paper explores the technical framework behind 
the implementation of the CNN model, feature extraction processes, and the distance-based recommendation system. 
It also delves into the efficacy of ResNet50 in feature representation and discusses the role of Euclidean distance in 
producing accurate and user-satisfactory outfit recommendations. 
Ultimately, the goal of this research is to provide users with a valuable tool that enhances their fashion 
choices and helps them discover new and exciting outfit combinations.

**Methodology **

**1. Image Input and Processing:**
   
o The user uploads three images each of top and bottom wear, which are processed using CV2 
(OpenCV), an essential library for image reading, sensing, resizing, and saving. These tasks ensure 
that the images are in proper shape and size for feature extraction.

o By using os and glob, the system reads files from specific directories and handles file paths 
efficiently, making it easy to manage large numbers of images in bulk. This ensures flexibility in the 
handling of user-uploaded content.

**2. Feature Extraction:**
   
o The backbone of the model's functionality is TensorFlow, which is used to extract deep features 
from the images through a pre-trained model like ResNet50. This process captures fine details from 
the images, such as textures, colors, cuts, and other stylistic elements, making them comparable in a 
mathematical feature space.

o Feature extraction allows the model to "understand" the images in a meaningful way, turning visual 
data into a vectorized representation suitable for further analysis.

**3. Combination Analysis:**
   
o Once the features of the images are extracted, the system generates all possible combinations of the 
three top wear and three bottom wear images (a total of nine combinations). 

o Euclidean distance is then calculated between these feature vectors to determine how visually 
compatible each combination is. The shorter the Euclidean distance between two vectors (top and 
bottom wear), the more visually harmonious the items are considered to be. 

o This ensures that the model considers not just individual fashion pieces, but also how well they work 
together as an outfit.

**4. Optimization and Pair Selection:**
   
o PHL (Parametric Hyperbolic Loss) is utilized to optimize the feature space, ensuring that the 
model effectively learns to minimize the Euclidean distance for visually compatible combinations. 

o Normalization techniques help standardize the input data, making sure that all features—such as 
color, texture, and pattern—are treated equally in the comparison process. This prevents any single 
feature from disproportionately influencing the final decision. 
NumPy is employed for efficient numerical computations, aiding in the rapid processing of image 
data, while os and glob handle the directory and file path management, ensuring smooth processing of 
multiple user-uploaded images

**Process Flow**

After the user selects the tops and bottoms on the website, the inputs are sent to the backend. Every image 
in tops and bottoms file is preprocessed and then combinations of outfits are formed. One by one features are 
extracted from outfit combinations formed and Euclidean distance is calculated with the dataset features file 
unless the minimum distance is found, In a dictionary, the outfit image path is stored along with the minimum 
Euclidean distance found and the dictionary is sorted, The top 2 or more (based on number of combinations 
formed) outfit combinations are displayed as ideal outfits.
