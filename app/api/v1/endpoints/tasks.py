## app/api/v1/endpoints/tasks.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from app.schemas.task import TaskCreate, Task, TaskUpdate
from app.services.task_service import TaskService
from app.db.session import get_db

router = APIRouter()

@router.post('/', response_model=Task, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    """
    try:
        created_task = TaskService.create_task(db, task.name, task.action)
        return created_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create task: {str(e)}")

@router.get('/{name}', response_model=Task)
def get_task(name: str, db: Session = Depends(get_db)):
    """
    Get a task by name.
    """
    try:
        task = TaskService.get_task(db, name)
        if not task:
            raise HTTPException(status_code=404, detail='Task not found')
        return task
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Task not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@router.put('/{name}', response_model=Task)
def update_task(name: str, task_update: TaskUpdate, db: Session = Depends(get_db)):
    """
    Update a task by name.
    """
    try:
        updated_task = TaskService.update_task(db, name, task_update)
        return updated_task
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Task not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update task: {str(e)}")

@router.delete('/{name}', status_code=204)
def delete_task(name: str, db: Session = Depends(get_db)):
    """
    Delete a task by name.
    """
    try:
        TaskService.delete_task(db, name)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Task not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete task: {str(e)}")
