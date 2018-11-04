// Abaqus_to_Gmsh.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include <iostream>
#include <fstream>
#include <string>
#include <locale>
#include <sstream>
#include <vector>

//This code is used to translate Abaqus input file (mesh) exported from BOLT to Gmsh format
//The first commit

//User instructions:
//get rid of the excessive *Elset. 

int main()
{
	int debug = 0; 

	int i, j, k;
	std::string filename;
	//std::cout << "input the file name here: " << std::endl;
	//std::getline(std::cin, filename, '\n');
	filename = "frigate_N=1_1ft.inp";
	std::ifstream infile;
	infile.open(filename);
	if (!infile) {
		std::cerr << "cannot open the file" << std::endl;
		exit(1);
	}
	//std::ofstream outFile;
	//outFile.open("output.msh"); //output Gmsh file
	std::vector<std::vector<std::string>> output;
	char buffer[256];
	std::string csvLine;
	int ct = -1;
	std::vector<int> sidesets_start;
	std::vector<int> sidesets_end;
	int nodestart = 0;
	int nodeend = 0;
	int elestart = 0;
	int eleend = 0;

	while (getline(infile, csvLine))
	{
		ct = ct + 1; //the current line number (starting from 0)
		std::istringstream csvStream(csvLine);
		std::vector<std::string> csvColumn;
		std::string csvElement;
		// read every element from the line that is seperated by commas
		// and put it into the vector or strings
		while (getline(csvStream, csvElement, ','))
		{
			csvColumn.push_back(csvElement);
		}
		output.push_back(csvColumn);
		if (csvColumn[0] == "*NODE" || csvColumn[0] == "*Node") {
			nodestart = ct + 1; //the node starts from the next line
		}
		if (csvColumn[0] == "*ELEMENT" || csvColumn[0] == "*Element") {
			//nodeend = ct - 3; //the line where the node definition ends
			nodeend = ct;
			elestart = ct + 1; //the line where element definition starts
		}
		if (csvColumn[0] == "*ELSET" || csvColumn[0] == "*Elset") {
			sidesets_start.push_back(ct + 1); //the line where sidesets (physical group) definition starts
			if (sidesets_start.size() == 1) {
				eleend = ct;
			}
		}
		if (csvColumn[0] == "*SURFACE" || csvColumn[0] == "*Surface") {
			sidesets_end.push_back(ct - 1); //the line where sidesets (physical group) definition ends
		}
		if (ct % 10000 == 0) {
			std::cout << ct << std::endl; //output which line is being read
		}
	}
	//search back to find where exactly does the node definition ends and redefine the value of nodeend. 
	//check if the first string of the line has a number in it. If so, this is the line we are looking for. 
	int flag = 0; 
	while (flag == 0) {
		for (i = 0; i < output[nodeend][0].size(); i++) {
			if (isdigit(output[nodeend][0].at(i))) {//check if the corresponding character in the first string is a digit
				flag = 1; 
			}
		}
		if (flag == 0) {
			nodeend = nodeend - 1;
		}
	}
	//search back to find where exactly does the element definition ends and redefine the value of element
	flag = 0;
	while (flag == 0) {
		/*
		for (i = 0; i < output[eleend][0].size(); i++) {
			if (isdigit(output[eleend][0].at(i))) {
				flag = 1;
			}
		}
		*/
		if (output[eleend].size() == 1 + 8) {
			flag = 1;
		}
		if (flag == 0) {
			eleend = eleend - 1;
		}
	}
	int NNODE = nodeend - nodestart + 1; //total node number
	int NEL = eleend - elestart + 1; //total element number
	double** GCOORD; //the vector to store the coordinate of nodes
	GCOORD = new double*[NNODE];
	for (i = 0; i < NNODE; i++) {
		GCOORD[i] = new double[3]; 
	}
	int**IEN; //element connectivity matrix
	IEN = new int*[NEL];
	for (i = 0; i < NEL; i++) {
		IEN[i] = new int[8]; 
	}


	double xoffset = 0.0;
	double yoffset = 0.0;
	double zoffset = 0.0;

	for (i = nodestart; i < nodeend + 1; i++) {
		GCOORD[i - nodestart][0] = stod(output[i][1]) + xoffset;
		GCOORD[i - nodestart][1] = stod(output[i][2]) + yoffset;
		GCOORD[i - nodestart][2] = stod(output[i][3]) + zoffset;
	}

	for (i = elestart; i < eleend + 1; i++) {
		for (j = 0; j < 8; j++) {
			IEN[i - elestart][j] = stoi(output[i][j + 1]); //change the string to integer
		}
	}

	//Store sidesets (physical group) elements
	int num_sidesets = sidesets_start.size();
	std::vector<std::vector<int>> sideset_ELE;
	for (i = 0; i < num_sidesets; i++) {
		std::vector<int> sideset_column;
		for (j = sidesets_start[i]; j < sidesets_end[i] + 1; j++) { //lines corresponding to the physical group i 
			//if (output[j].size == 3 && sidesets_end[i] == sidesets_start[i]) { //the element number is expressed as initial,end,internal way (only one line is used) 
			if (sidesets_end[i] == sidesets_start[i]) { //the element number is expressed as initial,end,internal way (only one line is used) 
				for (k = stoi(output[j][0]); k < stoi(output[j][1]) + 1; k += stoi(output[j][2])) {
					sideset_column.push_back(k);
				}
			}
			else {
				for (k = 0; k < output[j].size(); k++) { //store all members (k) in the line
					sideset_column.push_back(stoi(output[j][k]));
				}
			}
		}
		sideset_ELE.push_back(sideset_column); //Each sideset_column represents one physical group
	}

	//write Gmsh output file
	std::ofstream outfile;
	outfile.open("output.msh");
	if (!outfile) {
		std::cerr << "cannot open the file" << std::endl;
		exit(1);
	}
	outfile << "$MeshFormat" << std::endl;
	outfile << "2.2 0 8" << std::endl;
	outfile << "$EndMeshFormat" << std::endl;
	outfile << "$Nodes" << std::endl;
	//write nodes
	outfile << NNODE << std::endl;
	for (i = 0; i < NNODE; i++) {
		outfile << i + 1 << " " << GCOORD[i][0] << " " << GCOORD[i][1] << " " << GCOORD[i][2] << std::endl;
	}
	outfile << "$EndNode" << std::endl;
	//write elements (based on physical groups)
	outfile << "$Elements" << std::endl;
	//derive the total elements to be written in the file (in all physical groups)
	int totalele = 0;
	for (i = 0; i < num_sidesets; i++) {
		totalele += sideset_ELE[i].size();
	}
	totalele += NEL;
	outfile << totalele << std::endl;
	ct = 1;
	for (i = 0; i < num_sidesets; i++) { //different physical groups (3 stands for quad element)
		for (j = 0; j < sideset_ELE[i].size(); j++) { //loop through each element in the physical groups
			outfile << ct << " " << 3 << " " << 2 << " " << i + 1 << " " << 0 << " ";
			if (output[sidesets_end[i] + 2][1] == " S1") { //If the surface is S1
				outfile << IEN[sideset_ELE[i][j] - 1][0] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][1] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][2] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][3] << " ";
			}
			else if (output[sidesets_end[i] + 2][1] == " S2") { //If the surface is S2 
				outfile << IEN[sideset_ELE[i][j] - 1][4] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][5] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][6] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][7] << " ";
			}
			else if (output[sidesets_end[i] + 2][1] == " S3") { //If the surface is S3
				outfile << IEN[sideset_ELE[i][j] - 1][4] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][0] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][1] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][5] << " ";
			}
			else if (output[sidesets_end[i] + 2][1] == " S4") { //If the surface is S4
				outfile << IEN[sideset_ELE[i][j] - 1][5] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][1] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][2] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][6] << " ";
			}
			else if (output[sidesets_end[i] + 2][1] == " S5") { //If the surface is S5
				outfile << IEN[sideset_ELE[i][j] - 1][7] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][6] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][2] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][3] << " ";
			}
			else if (output[sidesets_end[i] + 2][1] == " S6") { //If the surface is S6
				outfile << IEN[sideset_ELE[i][j] - 1][4] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][7] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][3] << " ";
				outfile << IEN[sideset_ELE[i][j] - 1][0] << " ";
			}
			ct += 1;
			outfile << std::endl;
		}
	}
	//write elements (the whole domain, the last physical group)
	for (i = 0; i < NEL; i++) { //5 stands for hexahedral element
		outfile << ct << " " << 5 << " " << 2 << " " << num_sidesets + 1 << " " << 0 << " ";
		for (j = 0; j < 8; j++) {
			outfile << IEN[i][j] << " ";
		}
		ct += 1;
		outfile << std::endl;
	}
	outfile << "$EndElements" << std::endl;
    return 0;
}