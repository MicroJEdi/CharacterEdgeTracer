# CharacterEdgeTracer
Simple computer vision algorithm that finds text and converts characters into path vectors assuming that the wrttien characters are to be read top to bottom and left to right.
  * ↗ right & up diagonal movement is colored **blue**
  * ↘ right & down diagonal movement is colored **red**
  * **→** horizontal movement & **↓** vertical movement are colored **yellow**  
### Requirements
* ###### Python 2.7 (https://www.python.org/download/releases/2.7/)
* ###### PIL (http://www.pythonware.com/products/pil/)
### Python Script
* ###### CharacterTracer.py
  Converts the specified input image into the edge detected output image.
  * Sample input file (circuit.jpg)
    ![SampleInput](/python/circuit.jpg)
  * Sample segmented output file (circuitBlackAndWhite.JPEG)
    ![SampleSegmentedOutput](/python/circuitBlackAndWhite.JPEG)
  * Sample traced output file (circuitBlackAndWhite.JPEG)
    ![SampleTracedOutput](/python/circuitTraced.JPEG)
### TODO
* ###### Textual Representation of Path Vector

