#!/usr/bin/env python3
"""
Script to fix the prompt_llm function to handle tool calls properly.
"""
import json
import sys

def fix_notebook(notebook_path):
    with open(notebook_path, 'r') as f:
        nb = json.load(f)
    
    # Find the cell with prompt_llm function
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code' and 'source' in cell:
            source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
            if 'def prompt_llm' in source and 'tool_calls' not in source:
                print(f"Found prompt_llm function in cell {i}")
                
                # Replace the function
                new_source = '''def prompt_llm(messages, model="openai/GPT-4.1-mini", temperature=0, max_tokens=1000, tools=None, verbose=True):
    """
    Send a prompt or conversation to an LLM using LiteLLM and return the response.
    Handles tool calls by executing them and sending results back to the LLM.
    """
    import json
    
    # Map tool names to actual Python functions
    tool_functions = {
        "calculate_altitude": calculate_altitude
    }
    
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]
    if not (isinstance(temperature, (int, float)) and 0 <= temperature <= 2):
        raise ValueError("temperature must be a float between 0 and 2 (inclusive).")
    if not (isinstance(max_tokens, int) and max_tokens > 0):
        raise ValueError("max_tokens must be a positive integer.")

    try: 
        print("Contacting LLM via University Server...")
        max_iterations = 10  # Prevent infinite loops
        iteration = 0
        
        while iteration < max_iterations:
            response = litellm.completion(
                model=model,
                messages=messages,
                tools=tools,
                api_base=custom_api_base,
                api_key=astro1221_key,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            message = response['choices'][0]['message']
            
            # Check if the LLM wants to call a tool
            if 'tool_calls' in message and message['tool_calls']:
                if verbose:
                    print(f"\\nLLM requested {len(message['tool_calls'])} tool call(s)...")
                
                # Add the assistant's message (with tool calls) to the conversation
                messages.append(message)
                
                # Execute each tool call
                for tool_call in message['tool_calls']:
                    function_name = tool_call['function']['name']
                    function_args = json.loads(tool_call['function']['arguments'])
                    
                    if verbose:
                        print(f"  Calling {function_name} with args: {function_args}")
                    
                    # Execute the function
                    if function_name in tool_functions:
                        try:
                            func = tool_functions[function_name]
                            result = func(**function_args)
                            
                            # Add the tool result to the conversation
                            messages.append({
                                "role": "tool",
                                "tool_call_id": tool_call['id'],
                                "content": json.dumps({"result": result})
                            })
                            
                            if verbose:
                                print(f"  Result: {result}")
                        except Exception as e:
                            error_msg = f"Error executing {function_name}: {str(e)}"
                            if verbose:
                                print(f"  {error_msg}")
                            messages.append({
                                "role": "tool",
                                "tool_call_id": tool_call['id'],
                                "content": json.dumps({"error": error_msg})
                            })
                    else:
                        error_msg = f"Unknown function: {function_name}"
                        if verbose:
                            print(f"  {error_msg}")
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call['id'],
                            "content": json.dumps({"error": error_msg})
                        })
                
                iteration += 1
                continue  # Loop back to get the LLM's response to the tool results
            
            # No tool calls - we have the final answer
            answer = message.get('content', '')
            if verbose: 
                print(f"\\nSUCCESS! Here is the answer from {model}:\\n")
                print(answer if answer else "(No text response)")
            
            return response
            
        # If we've looped too many times
        print(f"\\nWARNING: Maximum iterations ({max_iterations}) reached.")
        return response
        
    except Exception as e:
        print(f"\\nERROR: Could not connect. Details:\\n{e}")    
        response = None
        return response
'''
                # Split into lines for notebook format
                cell['source'] = new_source.split('\n')
                print(f"Updated cell {i}")
                break
    
    # Also update calculate_altitude to handle string inputs
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code' and 'source' in cell:
            source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
            if 'def calculate_altitude' in source and 'isinstance(obj, str)' not in source:
                print(f"Found calculate_altitude function in cell {i}")
                # Add string handling at the beginning of the function
                lines = cell['source'] if isinstance(cell['source'], list) else cell['source'].split('\n')
                new_lines = []
                found_def = False
                for line in lines:
                    if 'def calculate_altitude' in line and not found_def:
                        new_lines.append(line)
                        found_def = True
                        # Add string handling code
                        new_lines.append('    # If obj is a string, try to map it to an AstroObject')
                        new_lines.append('    if isinstance(obj, str):')
                        new_lines.append('        obj = get_object_by_name(obj)')
                        new_lines.append('        if obj is None:')
                        new_lines.append('            raise ValueError(f"Could not find astronomical object: {obj}")')
                        new_lines.append('')
                    else:
                        new_lines.append(line)
                cell['source'] = new_lines
                print(f"Updated calculate_altitude in cell {i}")
                break
    
    # Save the notebook
    with open(notebook_path, 'w') as f:
        json.dump(nb, f, indent=1)
    print(f"Notebook updated: {notebook_path}")

if __name__ == '__main__':
    fix_notebook('Project_1.ipynb')
