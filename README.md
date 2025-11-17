# Task Management System Using LLM-Based Natural Language Processing
Submission Document
1. Introduction

This project implements a fully functional task management system that understands natural-language commands. It supports task extraction, priority detection, due-date parsing, task categorization, progress tracking, reminders, daily summaries, and task breakdown. The system uses the Gemini API for natural language processing, SQLite as the database, and Python for backend logic.

The implementation meets all assignment requirements for an LLM-powered task manager with a CLI interface and automated scheduling.

2. System Overview

The system allows the user to create tasks simply by typing natural-language instructions, such as:

"Remind me to finish the assignment by tomorrow morning."

The NLP component extracts structured data from natural language:

title

due_date

priority

category

The backend stores this data in a SQLite database, manages task status, and schedules reminders.

Additionally, the system can break down large tasks into subtasks and supports progress tracking through marking tasks as completed.

3. Architecture

The system follows a modular architecture:

task_manager/
    app.py
    gemini_nlp.py
    db.py
    scheduler.py
    date_parser.py
    requirements.txt
    .env

Component Responsibilities

app.py

Main application entry point

Handles CLI input

Routes commands to NLP, database, or scheduler

Manages user interaction

gemini_nlp.py

Handles all natural language processing

Extracts tasks into structured JSON

Breaks large tasks into subtasks

Cleans and validates JSON responses

db.py

Manages SQLite database

Creates tables

Inserts tasks

Retrieves pending and completed tasks

Marks tasks as done

scheduler.py

Schedules reminders

Runs daily summaries

Executes periodic jobs

date_parser.py

Converts natural language time expressions into datetime objects

Supports terms like today, tomorrow, morning, evening, weekdays

.env

Stores GEMINI_API_KEY securely

4. Database Design

SQLite database file: tasks.db

Table: tasks
Column	Type	Description
id	INTEGER	Primary key autoincrement
title	TEXT	Extracted task title
due_date	TEXT	Parsed due date in natural text
priority	TEXT	high, medium, or low
category	TEXT	work, personal, general
status	TEXT	pending or done

This structure satisfies all requirements for storage, retrieval, querying, and progress manipulation.

5. Natural Language Processing

The system uses Gemini 2.0 Flash API to interpret natural-language commands. The model is configured with strict instructions to always output structured JSON.

NLP Tasks

Task extraction
Converts natural input into a JSON object with fields:
title, due_date, priority, category.

Task breakdown
For commands beginning with "break down", the model generates a list of subtasks in valid JSON array format.

JSON cleaning and validation
Handles code-fenced output and extracts only valid JSON.

This modular NLP design ensures consistency, avoids runtime errors, and allows the scheduling module to use due dates reliably.

6. Backend Logic and Flow

Below is the system workflow:

User enters a command.

If the command begins with "break down", the system sends text to Gemini and displays subtasks.

Otherwise, NLP extracts task attributes.

Parsed task is inserted into SQLite.

If the task has a due date, a reminder is scheduled.

Daily summary is automatically printed at 9 AM.

User can list pending tasks, list completed tasks, or mark tasks as done.

Reminders are triggered at scheduled times.

This satisfies required functionality and productivity features.

7. Features Implemented

The following assignment requirements are fully met:

Task Management (required)

Natural language task creation

Priority detection

Due date parsing

Category assignment

Productivity Features (required)

Daily summaries

Task breakdown

Progress tracking (mark done)

Reminder system (scheduled notifications)

Technical Requirements

Python 3.8+

Gemini API for NLP

SQLite database

schedule library

CLI interface

# 8. Setup Guide

Create a folder named task_manager

Add all provided files

Install dependencies:

pip install -r requirements.txt


Create a .env file:

GEMINI_API_KEY=your_key_here


Run the application:

python app.py

9. Usage Examples

Below are sample commands supported by the system.

Create a task
remind me to study python tomorrow morning


System:

Task added: study python
Reminder scheduled for: tomorrow morning

Break down a large task
break down plan a birthday party

List pending tasks
list pending

Mark task as completed
mark done 3

List completed tasks
list done

Exit
exit

10. Conclusion

This project implements a complete task management assistant based on LLM-powered natural-language processing. It meets all assignment requirements including task parsing, NLP understanding, scheduling, progress tracking, and documentation. The modular architecture ensures extensibility, maintainability, and accurate task extraction.
