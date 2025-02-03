
import cv2 #camera ne kholva mate 
import mediapipe as mp #hands na detection mate 
import time #fps calc mate  

class HandDetector: #kai jagyae hand che ena mate  
    def __init__(self, mode=False, maxHands=2, modelComp=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelComp = modelComp
        '''
        mode: accuracy mate kaam aave 
        maxHands: Maximum ketla hand detect kari sake
        modelComp: Complexity aape higher complexity slower is the processing.
        detectionCon: Minimum confidence level for detecting a hand (default 0.5). aanathi niche hot to chances che k hand deect na thai
        trackCon: Minimum confidence for tracking a detected hand (default 0.5). aanathi niche hot to chances che k hand track thya pachi sathe rei 
        '''
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComp,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils #hand na landmarks ne drawkarva mate on the screen the red red dots 

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #color hoi bgr ma but open cv just rgb j samje or vice verse
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, 
                                               self.mpHands.HAND_CONNECTIONS)
        return img
    '''
    If hands are detected, it loops through them and draws landmarks (dots and connections) on the image.

    Returns the modified image with detected hands.

    aana karane red dots aave
    '''

    def findPosition(self, img, handNo=0, draw=True):
        lmList = [] #landmark ni list store karva mate
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            #the next loop is used to findthe pixel of the hand out of 21 coordinates from mediapipe 
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED) #circle aana karane aave on hand

        return lmList
            
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)


        cTime = time.time()
        fps = 1/(cTime-pTime) #logic for calculatiing fps
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, 
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)    

if __name__ == "__main__":
    main()
