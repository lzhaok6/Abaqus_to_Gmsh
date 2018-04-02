// Abaqus_to_Gmsh.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

//This code is used to translate Abaqus input file (mesh) exported from BOLT to Gmsh format

int main()
{
	int i, j, k;
	std::string filename;
	//std::cout << "input the file name here: " << std::endl;
	//std::getline(std::cin, filename, '\n');
	filename = "DDG_cuboid_fluidomain_6.01draft.inp";
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

		if (csvColumn[0] == "*NODE") {
			nodestart = ct + 1; //the node starts from the next line
		}
		if (csvColumn[0] == "*ELEMENT") {
			nodeend = ct - 3; //the line where the node definition ends
			elestart = ct + 1; //the line where element definition starts
		}
		if (csvColumn[0] == "********************************** S I D E S E T S **********************************") {
			eleend = ct - 2; //the line where element definition ends
		}
		if (csvColumn[0] == "*ELSET") {
			sidesets_start.push_back(ct + 1); //the line where sidesets (physical group) definition starts
		}
		if (csvColumn[0] == "*SURFACE") {
			sidesets_end.push_back(ct - 1); //the line where sidesets (physical group) definition ends
		}
		std::cout << ct << std::endl;
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

	for (i = nodestart; i < nodeend + 1; i++) {
		GCOORD[i - nodestart][0] = stod(output[i][1]);
		GCOORD[i - nodestart][1] = stod(output[i][2]);
		GCOORD[i - nodestart][2] = stod(output[i][3]);
	}
	for (i = elestart; i < eleend + 1; i++) {
		for (j = 0; j < 8; j++) {
			IEN[i - elestart][j] = stoi(output[i][j + 1]); //change the string to integer
		}
	}

	//output sidesets elements
	int num_sidesets = sidesets_start.size();
	std::vector<std::vector<int>> sideset_ELE;
	for (i = 0; i < num_sidesets; i++) {
		std::vector<int> sideset_column;
		for (j = sidesets_start[i]; j < sidesets_end[i] + 1; j++) {
			for (k = 0; k < output[j].size(); k++) {
				sideset_column.push_back(stoi(output[j][k]));
			}
		}
		sideset_ELE.push_back(sideset_column);
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
	for (i = 0; i < num_sidesets; i++) { //different physical groups (quad element)
		for (j = 0; j < sideset_ELE[i].size(); j++) { //loop through each element in the physical groups
			outfile << ct << " " << 3 << " " << 2 << " " << i + 1 << " " << 0 << " ";
			for (k = 4; k < 8; k++) { //Get the last four nodes in the element (assuming surface S2 in Abaqus input file (corresponding to the last four number in the element connectivity matrix), counter-clockwise)
				outfile << IEN[sideset_ELE[i][j] - 1][k] << " ";
			}
			ct += 1;
			outfile << std::endl;
		}
	}
	//write elements (the whole domain)
	for (i = 0; i < NEL; i++) {
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

