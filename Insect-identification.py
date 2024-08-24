import datetime
import time
import cv2
import os
import csv


def main():
    # image path
    image_path = r'C:\Users\ilan\projects\insect-identification\images\image_id_718.jpg'
    # current day for csv file
    current_date = str(datetime.date.today())
    # research location
    research_location = input("Please enter research location")
    # csv file type
    file_type = ".csv"
    csv_result = research_location + ' ' + current_date + file_type

    insects_identification(image_path, csv_result, research_location)


def insects_identification(image_path, output_path, research_location):
    start_time = time.time()
    # Receive the image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # convert the image to gray scale and apply Gaussian-blur filter
    gray_scale_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(gray_scale_filter, (5, 5), 0)

    # threshold the image
    _, thresh = cv2.threshold(gaussian_blur, 105, 255, cv2.THRESH_BINARY_INV)

    # find contours in the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # count the number of boxes
    number_of_boxes = 0

    # create a list to hold the bounding box coordinates
    boxes_list = []

    # loop through the contours
    for i, contour in enumerate(contours):
        # extract the coordinates (x,y), weight, and height of the contour's
        x, y, width, height = cv2.boundingRect(contour)
        # check if the contour is inside another contour (to avoid duplicate marks)
        inside = False
        for j in range(len(contours)):
            if i != j and cv2.pointPolygonTest(contours[j], (x, y), False) > 0:
                inside = True
                break

        # if the contour is not nested it will draw rectangle around it
        if not inside and (height > 29 and width > 29):
            number_of_boxes += 1
            # create bigger boxes, subtract value from coordinates and add it to height and width
            fit_box_rectangle = 25
            if x - fit_box_rectangle > 0 and y - fit_box_rectangle > 0:
                cv2.rectangle(image, (x - fit_box_rectangle, y - fit_box_rectangle),
                              (x + width + fit_box_rectangle, y + height + fit_box_rectangle), (0, 255, 0), 2)
                # add the bounding box coordinates to the list
                boxes_list.append(
                    (number_of_boxes, x - fit_box_rectangle, y - fit_box_rectangle, x + width + fit_box_rectangle,
                     y + height + fit_box_rectangle, research_location))
            else:
                cv2.rectangle(image, (x, y),
                              (x + width + fit_box_rectangle, y + height + fit_box_rectangle), (0, 255, 0), 2)
                boxes_list.append((number_of_boxes, x, y, width,
                                   height, research_location))

            # show number of box on output image
            cv2.putText(image, str(number_of_boxes), (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # create the output folder if it doesn't exist
    output_folder = os.path.join(os.getcwd(), 'output')

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # define the output file path for csv
    csv_output_path = os.path.join(output_folder, output_path)

    # write the bounding box coordinates to a CSV file
    with open(csv_output_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Box_ID', 'X', 'Y', 'Width', 'Height', 'Research_location'])
        for box in boxes_list:
            writer.writerow(box)

    # save the image with marked insects
    image_output_path = os.path.join(output_folder, 'output.jpeg')
    cv2.imwrite(image_output_path, image, [cv2.IMWRITE_JPEG_QUALITY, 99])

    end_time = time.time()
    print("Execution time: ", end_time - start_time, "seconds")


# insects_identification(path, csvOutPutName + file_type)

main()
